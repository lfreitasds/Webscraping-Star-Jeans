# Welcome to the Star Jeans Data Analysis
![alt text](https://github.com/lfreitas16/Webscraping-Star-Jeans/blob/main/star_jeans.jpg?raw=true)

## 1 - Business Problem

### 1.1 - Description

Star Jeans is a clothing company (fictional) owned by two Brazilian entrepreneurs Eduardo and Marcelo. After several successful businesses, they are planning to enter the US fashion market as an online eCommerce website.

To keep their operating costs down they will only sell men’s jeans at first. As they get more customers, they may grow their clothing brand.

With no experience in the fashion market, they don't know how to define the price, the models, the colors to design the products.

For this reason, they decided to hire our Data Science consultancy services to help on their decision-making.

### 1.2 - Data Overview

The data was collected from one of the Star Jeans main competitor's website using web scraping from March-?? 2022 through March-??? 2022. Below is a breakdown of the attributes:

| Attribute | Description |
| :----- | :----- |
| product_id | Unique ID for each product |
| style_id | Unique ID for each style |
| color_id | Unique ID for each color |
| product_name | Jeans' model |
| color_name | Jeans' color |
| fit | Jeans' fit |
| product_price | Product price |
| cotton | Cotton percentage |
| polyester | Polyester percentage |
| spandex | Spandex percentage |
| elastomultiester | Elastomultiester percentage |
| scrapy_datetime | Date stamp when data was collected |

Data source: [H&M Website](https://www2.hm.com/en_us/men/products/jeans.html)

## 2 - Business Assumptions

* OS MODELOS COM MAIS PRODUTOS PRODUTOS FORAM CONSIDERADOS OS MAIS POPULARES

* AS CORES COM MAIS PRODUTOS FORAM CONSIDERADOS AS MAIS POPULARES

* DDDD.

## 3 - Solution Strategy

**Step 01. Data Collection:** Use web scraping to collect data from the H&M's website. Web scraping is an automated method used to extract large amounts of data from websites. Hennes&Mauritz (H&M) is a retail firm that sells clothing and accessories at a fair price.

**Step 02. Data Cleaning:** It is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.

**Step 03. ETL Design:** ETL (Extract, Transform, Load) is an automated process which takes raw data, extracts the information required for analysis, transforms it into a format that can serve business needs, and loads it to a database.

* Design the ETL architecture.
* Define the dependencies between jobs. Sometimes the start of a job depends on the state of other jobs.
* Use Cron to schedule and run automatically the jobs. Cron runs in the background, and executes scheduled jobs known as “cron jobs”.
* Use the Python logging module to generate and store the Logs. The logging module lets you track events when your code runs so that when the code crashes you can check the logs and identify what caused it.

![ETL Architecture](https://github.com/lfreitas16/Webscraping-Star-Jeans/blob/main/ETL_architecture.jpg?raw=true)

**Step 04. Database Creation:** Create a new table in an SQLite database and insert records about the products.

**Step 05. Data Analysis:** Analyze each of the columns providing descriptive metrics for each attribute, obtaining a table with a statistical summary of the dataframe. 

**Step 06. Data Visualization:** Create different graphs to explore and better understand the data.


## 4 - Business Results

FALAR QUE PARA COMEÇAR ELES PODEM ESCOLHER OS MODELOS COM MAIS PRODUTOS
CALCULADO A MEDIANA DOS PREÇOS DOS PRODUTOS  
AGRUPANDO POR MODELO

**4.1 - Median price for the most used models:** 

| Item | Jeans' Model | Price (US$) |
| :-----: | :-----: | :-----: |
| 1 | Skinny Jeans | 19.99 |
| 2 | Slim Jeans | 19.99 |
| 3 | Regular Jeans | 19.99 |
| 4 | Skinny Cropped Jeans | 29.99 |
| 5 | Slim Tapered Jeans | 39.99 |

You can open the report with the median prices for all the models here:
[price_report.csv](https://github.com/lfreitas16/Webscraping-Star-Jeans/blob/main/price_report.csv)

**4.2 - The most used colors:** 

FALAR DO TOTAL DE CORES E
QUE ESSAS FORAM AS MAIS USADAS

| Item | Jeans' Color |
| :-----: | :----- |
| 1 | Light Denim Blue |
| 2 | Black |
| 3 | Denim Blue |
| 4 | Dark Denim Blue |
| 5 | Dark Gray |

You can find more information in the Project Notebook  
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
COLOCAR O LINK PARA O NOTEBOOK


## 5 - Conclusions

Web Scrapping is very appropriate for 
market trend analysis
gaining insights into a particular market

Web Scraping can be used by companies to scrap the product data 
fix the optimal pricing for their products so that they can obtain maximum revenue.

FALAR QUE DÁ PARA FAZER MONITORAMENTO AUTOMÁTICO
COM COLETA DE DADOS EM UM BANCO DE DADOS 

## 6 - Next Steps to Improve

* Desenvolver um sistema para controle dinâmico do preço do concorrente. Dynamic Price Monitoring
* Seria interessante para definir os produtos a ser lançados coletar também informações sobre os tamanhos.
* Coletar os dados diariamente por um mês, ou uma vez ao mês por um ano para observar a tendências  e o impacto da sazonalidade.

## 7 - Technologies

![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## 8 - Author

Leonardo de Freitas  
Aspiring Data Scientist
[GitHub Profile](https://github.com/lfreitas16/)
