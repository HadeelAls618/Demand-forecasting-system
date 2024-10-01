# Demand Forecasting System for FMCG Retailer
## Overview
This project showcases an end-to-end demand forecasting solution built to address the inventory management challenges faced by a large offline retailer selling Fast Moving Consumer Goods (FMCGs). Leveraging advanced machine learning techniques (XGBoost) and historical sales data, this system accurately predicts future demand for each product category, ensuring optimal inventory levels and reducing the risk of overstocking and understocking. This project serves as a demonstration of proficiency in Python, SQL, and handling large datasets

## Problem Statement
The retailer has been experiencing significant business losses due to inefficient inventory management, resulting in both overstocking and understocking of products. The key objective is to optimize inventory by predicting weekly demand for different product categories, enabling better alignment of supply with actual demand. This, in turn, will reduce storage costs, prevent lost sales, and improve overall profitability.

## Project Methodology
This project follows the CRISP-DM (Cross Industry Standard Process for Data Mining) framework, ensuring a structured and systematic approach through the following phases:
* **Business Understanding**: Define business objectives and identify pain points.
* **Data Understanding**: Collect, integrate, and analyze historical units sales data.
* **Data Preparation**: Clean and preprocess data using SQL and python.
* **Modeling**: Build and evaluate machine learning and time series models for demand forecasting.
* **Evaluation**: Assess model performance using key metrics (RMSLE) that is Good for inventory forecasting where relative error matters more than absolute differences.
* **Deployment**: Deploy the model using Streamlit for real-time demand predictions (you can check the app here)

## Data Sources
Three interconnected datasets were used in this project, providing a comprehensive view of sales, product characteristics, and store-level attributes:

**Product Data**: Product-specific information (UPC, description, manufacturer, category, size).
**Sales Data**: Weekly sales figures at the store level, promotions, discounts, units sold, and pricing.
**Store Data**: Store-level attributes including location, size, and market segmentation.
**The datasets were integrated using SQL in BigQuery, enabling a unified view for analysis and modeling**
