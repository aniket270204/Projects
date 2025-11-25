# 🛍️ Customer Shopping Behavior Analysis

A full data analytics project focused on understanding customer purchasing patterns using **Python, SQL, PostgreSQL, and Power BI**. This analysis uncovers insights related to spending behavior, product preferences, customer segments, and subscription impact — enabling informed business decision-making.

---

## 📌 Project Overview
This project analyzes **3,900 customer shopping transactions** to identify:

- Spending patterns and key revenue drivers  
- High-value customer segments  
- Top-performing categories and products  
- Discount and subscription influence on purchases  

The workflow covers **data cleaning → feature engineering → SQL analytics → dashboard visualization**.

---

## 📂 Dataset Summary
| Attribute | Details |
|----------|---------|
| Rows | 3,900 |
| Columns | 18 |
| Missing Values | 37 (Review Rating) |
| Data Includes | Age, Gender, Location, Item Purchased, Category, Purchase Amount, Season, Discount Applied, Previous Purchases, Review Rating, Shipping Type, etc. |

---

## 🛠️ Tech Stack
| Stage | Tools |
|-------|------|
| Data Cleaning & EDA | Python (Pandas, NumPy) |
| Database | PostgreSQL |
| Querying | SQL |
| Visualization | Power BI |

---

## 🧹 Data Processing & Feature Engineering (Python)
Key steps performed in preprocessing:

- Loaded dataset and performed summary exploration (`df.info()`, `.describe()`)
- Imputed missing values in **Review Rating** using **median per category**
- Standardized column naming to **snake_case**
- Created new attributes:
  - `age_group` from age bins
  - `purchase_frequency_days` from timestamps
- Removed redundant column `promo_code_used`
- Uploaded cleaned dataset into **PostgreSQL** for structured analysis

---

## 📊 SQL Business Insights
The following insights were extracted through SQL queries:

| Topic | Insight |
|-------|---------|
| Gender Revenue Split | Revenue comparison between male vs female customers |
| Discount Behavior | High-spending customers despite discounts |
| Product Quality | Top 5 products based on review ratings |
| Shipping Preference | Express vs Standard revenue differences |
| Subscription Value | Subscriber vs Non-subscriber spending & revenue share |
| Discount Dependency | Products that heavily rely on discounts |
| Customer Segmentation | New ▸ Returning ▸ Loyal classification |
| Category Leaders | Top 3 products based on purchase count per category |
| Subscription Pattern | Repeat buyers (>5 purchases) are more likely to subscribe |
| Age Group Revenue | Total revenue contribution by age groups |

---

## 📈 Dashboard — Power BI
The dashboard visualizes:

- Overall revenue and customer distribution  
- Category & product performance  
- Subscriber vs non-subscriber revenue  
- Discount & shipping trends  
- Demographic-based spend insights  

---

## 💡 Business Recommendations
| Recommendation | Impact |
|---------------|--------|
| Promote subscription benefits | Boost recurring purchases |
| Introduce loyalty programs | Increase retention |
| Reevaluate discount strategy | Maintain profit margins |
| Promote high-rated & top-selling products | Improve sales conversion |
| Target campaigns based on age & shipping preference | Improve marketing ROI |

---

## 📁 Project Structure
