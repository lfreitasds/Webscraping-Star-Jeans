# Imports
import os
import re
import logging
import sqlite3
import requests                         # pip install requests
import numpy  as np
import pandas as pd                     # pip install pandas
import math

from bs4        import BeautifulSoup    # pip install beautifulsoup4
from datetime   import datetime
from sqlalchemy import create_engine    # pip install sqlalchemy

# Data Collection
def data_collection( url, headers ):

    # Request to URL
    page = requests.get( url, headers=headers )

    # BeautifulSoup Object
    soup = BeautifulSoup( page.text, 'html.parser' )

    # Pagination
    total_item = soup.find_all('h2', class_='load-more-heading')[0].get('data-total')
    page_number = math.ceil(int(total_item) / 36)
    url02 = url + '?page-size=' + str(int(page_number * 36))

    # Request to URL02
    page = requests.get(url02, headers=headers)

    # BeautifulSoup Object
    soup = BeautifulSoup(page.text, 'html.parser')

    # ===================================== Product Data =====================================
    products = soup.find( 'ul', class_='products-listing small' )
    product_list = products.find_all( 'article', class_='hm-product-item' )

    # product id
    product_id = [p.get('data-articlecode') for p in product_list]

    # product category
    product_category = [p.get('data-category') for p in product_list]

    # product name
    product_list = products.find_all( 'a', class_="link" )
    product_name = [p.get_text() for p in product_list]

    # product price
    product_list = products.find_all( 'span', class_="price regular" )
    product_price = [p.get_text() for p in product_list]

    data = pd.DataFrame( [product_id, product_category, product_name, product_price] ).T
    data.columns = ['product_id', 'product_category', 'product_name', 'product_price']

    return data

# Data Collection by Product
def data_collection_by_product( data, headers ):

    # empty dataframe
    df_compositions = pd.DataFrame()

    # unique columns for all products
    aux = []

    df_pattern = pd.DataFrame(columns=['Art. No.', 'Composition', 'Fit'])

    for i in range(len(data)):

        # API requests
        url = 'https://www2.hm.com/en_us/productpage.' + data.loc[i, 'product_id'] + '.html'
        logger.debug( 'Product: %s', url )

        page = requests.get(url, headers=headers)

        # Beautiful Soup Object
        soup = BeautifulSoup(page.text, 'html.parser')

        # ================================= color name =========================================
        product_list = soup.find_all('a', class_='filter-option miniature active') + soup.find_all('a',
                                                                                                   class_='filter-option miniature ')

        # color name
        color_name = [p.get('data-color') for p in product_list]

        # product id
        product_id = [p.get('data-articlecode') for p in product_list]

        df_color = pd.DataFrame([product_id, color_name]).T
        df_color.columns = ['product_id', 'color_name']

        for j in range(len(df_color)):
            # API requests
            url = 'https://www2.hm.com/en_us/productpage.' + df_color.loc[j, 'product_id'] + '.html'

            logger.debug( 'Color: %s', url )

            page = requests.get(url, headers=headers)

            # Beautiful Soup Object
            soup = BeautifulSoup(page.text, 'html.parser')

            # ============================== Product Name ==========================================
            product_name = soup.find_all('h1', class_='primary product-item-headline')
            product_name = product_name[0].get_text()

            # ============================== Product Price ==========================================
            product_price = soup.find_all('div', class_='primary-row product-item-price')
            product_price = re.findall(r'\d+\.?\d+', product_price[0].get_text())[0]

            # =============================== composition ==========================================
            product_composition_list = soup.find_all('div', class_='details-attributes-list-item')
            product_composition = [list(filter(None, p.get_text().split('\n'))) for p in product_composition_list]

            # rename dataframe
            df_composition = pd.DataFrame(product_composition).T
            df_composition.columns = df_composition.iloc[0]

            # delete first row & complete where none
            df_composition = df_composition.iloc[1:].fillna(method='ffill')

            # remove pocket, pocket lining, shell and lining
            df_composition['Composition'] = df_composition['Composition'].replace('Pocket: ', '', regex=True)
            df_composition['Composition'] = df_composition['Composition'].replace('Pocket lining: ', '', regex=True)
            df_composition['Composition'] = df_composition['Composition'].replace('Shell: ', '', regex=True)
            df_composition['Composition'] = df_composition['Composition'].replace('Lining: ', '', regex=True)

            # guarantee the same number of columns
            df_composition = pd.concat([df_pattern, df_composition], axis=0)

            # deleting unnecessary columns
            df_composition = df_composition.drop(df_composition.iloc[:, 3:], axis=1)

            # rename columns
            df_composition.columns = ['product_id', 'composition', 'fit']
            df_composition['product_name'] = product_name
            df_composition['product_price'] = product_price

            # keep new columns if it shows up
            aux = aux + df_composition.columns.tolist()

            # merge df_composition + df_color
            df_composition = pd.merge(df_composition, df_color, how='left', on='product_id')

            # all products
            df_compositions = pd.concat([df_compositions, df_composition], axis=0)

    # Join Showroom data + Details
    df_compositions['style_id'] = df_compositions['product_id'].apply(lambda x: x[:-3])
    df_compositions['color_id'] = df_compositions['product_id'].apply(lambda x: x[-3:])

    # scrapy datetime
    df_compositions['scrapy_datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return df_compositions

# Data Cleaning
def data_cleaning( df_compositions ):

    # product_id
    df_data = df_compositions.dropna(subset=['product_id'])

    # product_name
    df_data['product_name'] = df_data['product_name'].str.replace( '\n', '' )
    df_data['product_name'] = df_data['product_name'].str.replace( '\t', '' )
    df_data['product_name'] = df_data['product_name'].str.replace( '  ', '' )
    df_data['product_name'] = df_data['product_name'].str.replace( ' ', '_' ).str.lower()

    # product_price
    df_data['product_price'] = df_data['product_price'].astype(float)

    # color_name
    df_data['color_name'] = df_data['color_name'].str.replace( ' ','_' ).str.lower()

    # fit
    df_data['fit'] = df_data['fit'].str.replace( ' ','_' ).str.lower()

    # drop duplicates
    df_data = df_data.drop_duplicates( subset=['product_id', 'composition', 'fit', 'product_name', 'product_price', 'color_name', 'style_id', 'color_id', 'scrapy_datetime'], keep='last' )

    # reset index
    #data = data.reset_index( drop=True )

    # break composition by comma
    df1 = df_data['composition'].str.split( ',', expand=True ).reset_index(drop=True)

    # cotton | polyester | spandex  | elastomultiester
    df_ref = pd.DataFrame( index=np.arange( len(df_data) ), columns=['cotton', 'polyester', 'spandex', 'elastomultiester'] )

    # =============================== composition ==========================================

    # ---------- cotton ----------
    df_cotton_0 = df1.loc[df1[0].str.contains( 'Cotton', na=True ), 0]
    df_cotton_0.name = 'cotton'

    df_cotton_1 = df1.loc[df1[1].str.contains( 'Cotton', na=True ), 1]
    df_cotton_1.name = 'cotton'

    # combine

    df_cotton = df_cotton_0.combine_first( df_cotton_1 )

    df_ref = pd.concat( [df_ref, df_cotton ], axis=1 )
    df_ref = df_ref.iloc[:, ~df_ref.columns.duplicated( keep='last' )]

    # ---------- polyester ----------
    df_polyester_0 = df1.loc[df1[0].str.contains('Polyester', na=True), 0]
    df_polyester_0.name = 'polyester'

    df_polyester_1 = df1.loc[df1[1].str.contains('Polyester', na=True), 1]
    df_polyester_1.name = 'polyester'

    # combine

    df_polyester = df_polyester_0.combine_first( df_polyester_1 )

    df_ref = pd.concat( [df_ref, df_polyester], axis=1 )
    df_ref = df_ref.iloc[:, ~df_ref.columns.duplicated( keep='last' )]

    # ---------- spandex ----------
    df_spandex_1 = df1.loc[df1[1].str.contains('Spandex', na=True), 1]
    df_spandex_1.name = 'spandex'

    df_spandex_2 = df1.loc[df1[2].str.contains('Spandex', na=True), 2]
    df_spandex_2.name = 'spandex'

    # combine

    df_spandex = df_spandex_1.combine_first( df_spandex_2 )

    df_ref = pd.concat( [df_ref, df_spandex], axis=1 )
    df_ref = df_ref.iloc[:, ~df_ref.columns.duplicated( keep='last' )]

    # ---------- elastomultiester ----------
    df_elastomultiester = df1.loc[df1[1].str.contains('Elastomultiester', na=True), 1]
    df_elastomultiester.name = 'elastomultiester'

    df_ref = pd.concat( [df_ref, df_elastomultiester], axis=1 )
    df_ref = df_ref.iloc[:, ~df_ref.columns.duplicated( keep='last' )]

    # join of combine with product_id
    df_aux = pd.concat( [df_data['product_id'].reset_index(drop=True), df_ref], axis=1 )

    # format composition data
    df_aux['cotton']     = df_aux['cotton'].apply( lambda x: int( re.search( '\d+', x ).group(0)) / 100 if pd.notnull( x ) else x)
    df_aux['polyester']  = df_aux['polyester'].apply( lambda x: int( re.search( '\d+', x ).group(0)) / 100 if pd.notnull( x ) else x)
    df_aux['spandex']   = df_aux['spandex'].apply( lambda x: int( re.search( '\d+', x ).group(0)) / 100 if pd.notnull( x ) else x)
    df_aux['elastomultiester'] = df_aux['elastomultiester'].apply( lambda x: int( re.search( '\d+', x ).group(0)) / 100 if pd.notnull( x ) else x)

    # final join
    df_aux = df_aux.groupby( 'product_id' ).max().reset_index().fillna(0)
    df_data = pd.merge( df_data, df_aux, on='product_id', how='left' )

    # Drop columns
    df_data = df_data.drop( columns=['composition'], axis=1 )

    # drop duplicates
    df_data = df_data.drop_duplicates()

    return df_data

# Data Insert
def data_insert( df_data ):

    data_insert = df_data[[
        'product_id',
        'style_id',
        'color_id',
        'product_name',
        'color_name',
        'fit',
        'product_price',
        'cotton',
        'polyester',
        'spandex',
        'elastomultiester',
        'scrapy_datetime'
    ]]

    # create database connection
    conn = create_engine( 'sqlite:///database_hm.sqlite', echo=False )

    # data insert
    data_insert.to_sql( 'vitrine', con=conn, if_exists='append', index=False )

    return None

if __name__ == '__main__':
    # logging
    path = "C:/repos/curso_python_ds_ao_dev/"

    if not os.path.exists( path + 'Logs' ):
        os.makedirs( path + 'Logs' )

    logging.basicConfig(
        filename= path + 'Logs\webscraping_hm.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger( 'webscraping_hm' )

    # parameters and constants
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # URL
    url = 'https://www2.hm.com/en_us/men/products/jeans.html'

    # data collection
    data = data_collection( url, headers )
    logger.info( 'Data collection done' )

    # data collection by product
    df_compositions = data_collection_by_product( data, headers )
    logger.info( 'Data collection by product done' )

    # data cleaning
    df_data = data_cleaning( df_compositions )
    logger.info( 'Data product cleaned done' )

    # data insertion
    data_insert( df_data )
    logger.info( 'Data insertion done' )