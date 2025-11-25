🛍️ Customer Shopping Behavior Analysis 
📌 Project Overview

This project analyzes 3,900 customer shopping transactions to uncover patterns in spending, segmentation,
product preferences, and subscription behavior.
Insights derived from this analysis can support data-driven decision-making in marketing,
inventory planning, and customer retention.




📂 Dataset Summary

Details Information 

Rows           = 3,900 
Columns        = 18 
Missing Values = 37 (Review Rating) 
Key Features   = Age, Gender, Subscription Status, Item Purchased,
                 Category, Season, Purchase Amount, Discount Applied,
                 Frequency, Review Rating, Shipping Type, etc.




🔧 Tech Stack

Stage Technologies Data Cleaning & Prep Python (Pandas, NumPy) Database 
Integration PostgreSQL Analytical Queries SQL Data Visualization Power BI



🧹 Data Processing & Feature Engineering (Python)

- Major preprocessing tasks included
- Importing dataset and basic exploration (df.info(), .describe())
- Handling missing values — Imputed Review Rating using median per category
- Column standardization to snake_case
- Feature engineering:
- age_group based on customer age ranges
- purchase_frequency_days from transaction timestamps
- Removed redundant column: promo_code_used
- Loaded cleaned dataset into PostgreSQL for SQL-based analysis





📊 SQL-Based Business Analysis

Key insights extracted from PostgreSQL queries include:

✔ Revenue comparison between male and female customers
✔ High-spending customers who used discounts 
✔ Top 5 products by average rating 
✔ Express vs. Standard shipping revenue differences 
✔ Subscriber vs. Non-subscriber spending analysis 
✔ Products most dependent on discounts 
✔ Customer segmentation: New, Returning, Loyal 
✔ Top 3 most purchased products in each category 
✔ Subscription likelihood among repeat buyers (>5 purchases) 
✔ Revenue contribution by age groups 





📈 Dashboard — Power BI

An interactive Power BI dashboard was built to visualize:

   - Total revenue breakdowns
   - Product & category performance
   - Subscription and discount trends
   - Demographic-based customer spending




💡 Business Recommendations

Based on the findings:

Recommendation Purpose:
- Promote subscription benefits Boost recurring customers
- Loyalty rewards for frequent buyers Increase retention
- Review discount strategy Maintain revenue margins
- Highlight best-rated & best-selling products Improve product positioning
- Target marketing by age & shipping preferences Maximize conversion efficiency
