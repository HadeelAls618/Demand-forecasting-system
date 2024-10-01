# Demand Forecasting System for FMCG Retailer
## Overview
This project showcases an end-to-end demand forecasting solution built to address the inventory management challenges faced by a large offline retailer selling Fast Moving Consumer Goods (FMCGs). Leveraging advanced machine learning techniques (XGBoost) and historical sales data, this system accurately predicts future demand for each product category, ensuring optimal inventory levels and reducing the risk of overstocking and understocking. This project serves as a demonstration of expertise in data manipulation, machine learning, and web deployment.


## Problem Statement
The retailer has been experiencing significant business losses due to inefficient inventory management, resulting in both overstocking and understocking of products. The key objective is to optimize inventory by predicting weekly demand for different product categories, enabling better alignment of supply with actual demand. This, in turn, will reduce storage costs, prevent lost sales, and improve overall profitability.

## Project Methodology
This project follows the CRISP-DM (Cross Industry Standard Process for Data Mining) framework, ensuring a structured approach to address the business problem through the following phases:
* **Business Understanding:**
Defined the business objectives by identifying key pain points related to inventory management for a large FMCG retailer, focusing on optimizing stock levels to prevent overstocking and understocking.

* **Data Understanding & Integration:**
Utilized **BigQuery** as the primary data storage solution and integrated it with Google Colab for seamless data handling using both **SQL** and **Python**. This setup enabled efficient data processing and analysis, allowing for comprehensive insights through a combination of SQL queries and Python libraries.

* **Data Preparation:**
Conducted Exploratory Data Analysis (**EDA**) using both SQL and Python. Applied **time-series feature engineering** techniques, such as lags and moving averages, to capture seasonality and trends in sales data.

* **Modeling & Evaluation:**
Built a robust time-series demand forecasting model using XGBoost, selected for its efficiency in handling structured data. The model was evaluated using Root Mean Squared Logarithmic Error (RMSLE), a metric particularly suitable for inventory forecasting where relative error matters more than absolute differences.

* **Deployment:**
Developed an interactive web application using **Streamlit**, enabling stakeholders to view predicted demand for each product category in **real-time**. This deployment completes the full cycle of our project. you can check the app [here](https://demand-forecasting-system-c3m3c2cxxz6z6fnatgasmv.streamlit.app/)

## Data Sources
Three interconnected datasets were used in this project, providing a comprehensive view of sales, product characteristics, and store-level attributes:

* **Product Data**: Product-specific information (UPC, description, manufacturer, category, size).
* **Sales Data**: Weekly sales figures at the store level, promotions, discounts, units sold, and pricing.
* **Store Data**: Store-level attributes including location, size, and market segmentation.
  
**The datasets were integrated using SQL in BigQuery, enabling a unified view for analysis and modeling**

### Future Directions
Planned enhancements include implementing real-time demand tracking using Airflow and BigQuery and exploring advanced deep learning techniques, such as LSTMs, for capturing long-term dependencies.

  ## Contact
If you have any questions or would like to discuss this project further, feel free to reach out!
* [LinkedIn](https://www.linkedin.com/in/hadeel-als-0a23702a6?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app ) :
* Email: alsadonhadeel@gmail.com
