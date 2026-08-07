# 📊 Sales Performance Dashboard

An end-to-end **Data Analysis** project that demonstrates the complete analytics workflow—from raw sales data to business insights and interactive dashboards using **Python, SQL, SQLite, and Power BI**.

This project is being built while learning industry-standard data analysis tools and best practices commonly used by Data Analysts.

---

# 🚀 Project Objective

The objective of this project is to analyze retail sales data and answer real business questions through:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL Analysis
- Business KPI Calculation
- Interactive Dashboard Development
- Business Insight Generation

---

# 🛠️ Tech Stack

### Programming
- Python

### Python Libraries
- Pandas
- NumPy
- Matplotlib
- OpenPyXL

### Database
- SQLite

### Query Language
- SQL

### Data Visualization
- Power BI

### Version Control
- Git
- GitHub

---

# 📂 Project Structure

```text
sales-performance-dashboard/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── database/
│   └── sales.db
│
├── scripts/
│   ├── 01_data_cleaning.py
│   ├── 02_create_database.py
│   └── 03_sql_analysis.py
│
├── sql/
│   └── queries.sql
│
├── dashboard/
│   └── Sales_Performance_Dashboard.pbix
│
├── screenshots/
│   └── day3_dashboard.png
│
├── business_insights.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📈 Dataset Information

**Dataset:** Superstore Sales Dataset

- **Total Records:** 9,994
- **Total Columns:** 21

### Main Features

- Orders
- Customers
- Products
- Category
- Sub-Category
- Region
- Sales
- Profit
- Discount
- Quantity
- Order Date
- Ship Date

---

# 📅 Project Progress

## ✅ Day 1 – Data Cleaning & Preparation

### Completed

- Project setup
- Installed required libraries
- Loaded Superstore dataset
- Performed Exploratory Data Analysis (EDA)
- Checked data types
- Checked missing values
- Checked duplicate records
- Converted date columns to datetime
- Created Year and Month columns
- Created additional calculated fields
- Saved cleaned dataset

### Skills Learned

- Reading CSV files using Pandas
- Working with DataFrames
- Data Cleaning
- Exploratory Data Analysis
- DateTime conversion
- Feature Engineering
- Exporting cleaned datasets

---

## ✅ Day 2 – SQL Analysis & Business Insights

### Completed

- Created SQLite database
- Imported cleaned dataset into SQLite
- Connected Python with SQLite
- Wrote **25+ SQL queries**
- Calculated business KPIs
- Performed sales and profit analysis by:
  - Category
  - Sub-Category
  - Region
  - Customer
  - Product
- Used filtering and aggregation to answer business questions

### SQL Concepts Practiced

- `SELECT`
- `WHERE`
- `GROUP BY`
- `ORDER BY`
- `LIMIT`
- `HAVING`
- Aggregate Functions:
  - `COUNT()`
  - `SUM()`
  - `AVG()`
  - `MAX()`
  - `MIN()`
- `ROUND()`
- `NULLIF()`
- `AND`
- `OR`
- `IN`

---

## ✅ Day 3 – Power BI Dashboard

### Completed

- Installed and configured Power BI Desktop
- Loaded the cleaned Superstore dataset into Power BI
- Created DAX measures for business KPIs
- Created KPI cards for:
  - Total Sales
  - Total Profit
  - Total Orders
  - Average Sales
  - Profit Margin %
- Created **Sales Trend Over Time** visualization
- Created **Sales by Category** visualization
- Created **Profit by Region** visualization
- Created **Sales by Customer Segment** visualization
- Started **Top Customers by Sales** analysis
- Practiced dashboard layout and visual formatting

### Power BI Concepts Learned

- Importing data into Power BI
- DAX measures
- KPI cards
- Line charts
- Column charts
- Bar charts
- Donut charts
- Top N filtering
- Basic dashboard design
- Visual formatting

---

# 📌 Business Questions

The project explores questions such as:

- How many total orders were placed?
- What is the total sales revenue?
- What is the total profit?
- How are sales changing over time?
- Which category generates the highest sales?
- Which region generates the highest profit?
- Which customer segment generates the most sales?
- Who are the top customers by sales?
- Which products generate the highest revenue?
- Which orders resulted in losses?
- Which shipping mode is most frequently used?

---

# 📊 Business KPIs

The dashboard currently includes:

| KPI | Description |
|---|---|
| Total Sales | Total revenue generated |
| Total Profit | Total profit generated |
| Total Orders | Number of orders/records |
| Average Sales | Average sales value |
| Profit Margin % | Profit as a percentage of sales |

Additional analysis includes:

- Sales by Category
- Profit by Region
- Sales by Customer Segment
- Sales Trend Over Time
- Top Customers by Sales

---

# 📈 Dashboard Visualizations

The Power BI dashboard currently contains:

### KPI Cards

- Total Sales
- Total Profit
- Total Orders
- Average Sales
- Profit Margin %

### Charts

- Sales Trend Over Time
- Sales by Category
- Profit by Region
- Sales by Customer Segment
- Top Customers by Sales

### Upcoming Interactive Features

- Year slicer
- Region slicer
- Category slicer
- Interactive filtering

---

# 💼 Skills Demonstrated

### Data Analysis

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Business KPI Analysis
- Data Visualization
- Data Storytelling

### Python

- Pandas
- NumPy
- Matplotlib
- SQLite integration

### SQL

- Data aggregation
- Filtering
- Grouping
- Sorting
- Business analysis queries

### Power BI

- DAX Measures
- KPI Cards
- Interactive Visualizations
- Dashboard Design
- Top N Analysis

### Other Tools

- Git
- GitHub
- Jupyter Notebook
- SQLite

---

# 🔜 Upcoming Work

## Day 4 – Finalization

- Complete Top 10 Customers visualization
- Add interactive slicers
- Improve dashboard layout
- Apply final formatting
- Validate dashboard calculations
- Generate final business insights
- Add dashboard screenshots
- Improve README documentation
- Clean and organize GitHub repository
- Prepare the project for portfolio/interview presentation

---

# 📷 Dashboard Preview

### Current Dashboard – Day 3

![Sales Performance Dashboard](screenshots/day3_dashboard.png)

> The dashboard will be further refined with interactive slicers, improved formatting, and additional analysis on Day 4.

---

# ▶️ How to Run

## 1. Clone the repository

```bash
git clone <repository-url>
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the data cleaning script

```bash
python scripts/01_data_cleaning.py
```

## 4. Create the SQLite database

```bash
python scripts/02_create_database.py
```

## 5. Run SQL analysis

```bash
python scripts/03_sql_analysis.py
```

## 6. Open the Power BI dashboard

Open:

```text
dashboard/Sales_Performance_Dashboard.pbix
```

using **Power BI Desktop**.

---

# 🗓️ Project Timeline

| Day | Focus | Status |
|---|---|---|
| Day 1 | Data Cleaning & Preparation | ✅ Completed |
| Day 2 | SQL Analysis & Business Questions | ✅ Completed |
| Day 3 | Power BI Dashboard Development | ✅ Completed |
| Day 4 | Dashboard Finalization & Insights | 🔜 Upcoming |

---

# 👩‍💻 Author

**Sadikshya Adhikari**

Computer Engineering Student | Aspiring Data Analyst | AI & ML Enthusiast