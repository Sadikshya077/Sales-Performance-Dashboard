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

- Power BI *(In Progress)*

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
│
├── screenshots/
│
├── business_insights.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📈 Dataset Information

**Dataset:** Superstore Sales Dataset

- Total Records: **9,994**
- Total Columns: **21**

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
- Saved cleaned dataset

### Skills Learned

- Reading CSV files using Pandas
- DataFrames
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
- Wrote 25+ SQL queries
- Calculated business KPIs
- Performed sales analysis by:
  - Category
  - Region
  - Customer
  - Product
- Generated business insights

### SQL Concepts Practiced

- SELECT
- WHERE
- GROUP BY
- ORDER BY
- LIMIT
- HAVING
- Aggregate Functions
  - COUNT()
  - SUM()
  - AVG()
  - MAX()
  - MIN()
- ROUND()
- NULLIF()
- AND / OR / IN

---

# 📊 Key Business Questions Answered

Some of the business questions explored in this project include:

- How many total orders were placed?
- What is the total sales revenue?
- What is the total profit?
- Which category generates the highest sales?
- Which region is the most profitable?
- Who are the top customers by sales?
- Which products generate the highest revenue?
- Which orders resulted in losses?
- Which shipping mode is most frequently used?

---

# 📌 Business KPIs

The following KPIs were calculated using SQL:

- Total Orders
- Total Sales
- Total Profit
- Average Sales
- Highest Sale
- Lowest Sale
- Sales by Category
- Profit by Region
- Top Customers
- Top Products

---

# 🔜 Upcoming Work

## Day 3

- Connect dataset to Power BI
- Create KPI cards
- Build interactive charts
- Add slicers and filters
- Design professional dashboard layout

## Day 4

- Dashboard refinement
- Final business insights
- README improvements
- GitHub project polishing

---

# 💼 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- SQL Query Writing
- Database Management
- Business KPI Analysis
- Data Storytelling
- Git & GitHub

---

# 📷 Dashboard Preview

*(Will be added after completing the Power BI dashboard.)*

---

# ▶️ How to Run

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the scripts in order

```bash
python scripts/01_data_cleaning.py
python scripts/02_create_database.py
python scripts/03_sql_analysis.py
```

---

# 👩‍💻 Author

**Sadikshya Adhikari**

Computer Engineering Student | Aspiring Data Analyst | AI & ML Enthusiast