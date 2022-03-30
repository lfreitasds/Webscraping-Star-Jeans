# Welcome to the Star Jeans Data Analysis
![alt text](https://github.com/lfreitas16/Webscraping-Star-Jeans/blob/main/star_jeans.jpg?raw=true)

## 1 - Business Problem

### 1.1 - Description

Star Jeans is a clothing company (fictional) owned by two Brazilian entrepreneurs Eduardo and Marcelo. After several successful businesses, they are planning to enter the US fashion market as an online e-commerce website.

Initially, they will only sell men’s jeans to keep their operating costs down. As they get more customers, they plan to grow their clothing brand.

They already know the entry product and the target audience, but they lack experience in the fashion market and, therefore, don't know how to define the price, type of pants, and the raw material needed to manufacture the products.

For this reason, they decided to hire our Data Science consultancy to answer the following questions:

1. What is the best selling price for the pants?
2. How many models should they sell in the initial production?
3. What are the raw materials needed to manufacture the pants?

### 1.2 - Data Overview

The data was collected from one of the Star Jeans main competitor's website using web scraping from March-?? 2022 through March-??? 2022. Below is a breakdown of the attributes:

| Attribute | Description |
| :----- | :----- |
| product_id | Unique ID for each product |
| style_id | Unique ID for each model |
| color_id | Unique ID for each color |
| product_name | Product name |
| color_name | Jeans' Color |
| fit | Jeans' fit |
| product_price | Product price |
| cotton | Cotton percentage |
| polyester | Polyester percentage |
| spandex | Spandex percentage |
| elastomultiester | Elastomultiester percentage |
| scrapy_datetime | Date stamp when data was collected |

Data source: [H&M Website](https://www2.hm.com/en_us/men/products/jeans.html)

## 2 - Business Assumptions

* AAAAA.

* BBBB.

* CCCC.

* DDDD.

## 3 - Solution Strategy

**Step 01. Data Collection:** Use web scraping to collect data from the H&M's website. Web scraping is an automated method used to extract large amounts of data from websites.
Hennes&Mauritz (H&M) group is headquartered in Sweden. It is a retail firm that sells clothing and accessories at a fair price.

**Step 02. Data Cleaning:** It is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.

**Step 03. ETL Design:** ETL (Extract, Transform, Load) is an automated process which takes raw data, extracts the information required for analysis, transforms it into a format that can serve business needs, and loads it to a database.

* Design the ETL architecture.
* Define the dependencies between jobs. Sometimes the start of a job depends on the state of other jobs.
* Use Cron to schedule and run automatically the jobs. Cron runs in the background, and executes scheduled jobs known as “cron jobs”.
* Use the Python logging module to generate and store the Logs. The logging module lets you track events when your code runs so that when the code crashes you can check the logs and identify what caused it.

![ETL Architecture](https://github.com/lfreitas16/Webscraping-Star-Jeans/blob/main/ETL_architecture.jpg?raw=true)

**Step 04. Database Creation:** Create a new table in an SQLite database and insert records about the products. To create a new table you use the following steps:

* First, create a Connection object using the connect() function of the sqlite3 module.
* Second, create a Cursor object by calling the cursor() method of the Connection object.
* Third, pass the CREATE TABLE statement to the execute() method of the Cursor object and execute this method.

**Step 05. Data Analysis:** Analyze each of the columns providing descriptive metrics for each attribute, obtaining a table with a statistical summary of the dataframe. 

**Step 06. Data Visualization:** Create different graphs to explore and better understand our data. **ESCREVER UM RESUMO DOS GRÁFICOS USADOS AQUI**

**Step 07. Recommendation Report:** **ESCREVER UM RESUMO DA PLANILHA** Deliver the final product.

You can open the report here: [recommendation_report.csv](https://github.com/lfreitas16/Insights-House-Rocket/blob/main/report_sale_price.csv)

You can find more information in the Project Notebook  
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

## 4 - Business Results
The sale price was calculated for two situations:  
1 - AAAA.  
2 - BBBB.  

– Precificação de produto.
– Preço ótimo para maximizar o lucro.

**LISTAR O PRINCIPAIS PRODUTOS E COMO CHEGOU NO RESULTADO**

| Sale Condition | No of Homes | Total Cost (US$) | Sales Revenue (US$) | Profit (US$) |
| :-----: | :-----: | :-----: | :-----: | :-----: |
|1 |10682 |4,119,644,414.00 |5,355,537,738.20 |1,235,893,324.20 |
| 2 | 10931 | 7,553,280,594.00 | 8,333,846,174.20 | 780,565,580.20 |
| Grand Total | 21613 | 11,672,925,008.00 | 13,689,383,912.40 | 2,016,458,904.40 |

## 5 - Conclusions
Web Scrapping is very appropriate for 
market trend analysis
gaining insights into a particular market

Web Scraping can be used by companies to scrap the product data 
fix the optimal pricing for their products so that they can obtain maximum revenue.

## 6 - Next Steps to Improve

Dynamic Price Monitoring

## 7 - Technologies

![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## 8 - Author

Leonardo de Freitas  
Aspiring Data Scientist
[GitHub Profile](https://github.com/lfreitas16/)
