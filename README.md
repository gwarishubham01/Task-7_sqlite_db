# 📊 Sales Analysis Project (SQLite + Python)

This project demonstrates how to perform basic sales data analysis using SQL queries in Python, with visual output using bar charts.

---


## 🚀 Features

- Connect to an SQLite database
- Execute SQL queries stored in an external `.sql` file
- Load results into a Pandas DataFrame
- Display and save bar charts for revenue by product

---

## 🛠️ Requirements

Install Python dependencies via pip:

```bash
pip install pandas matplotlib
```


---

## 📌 How to Run

1. Make sure the database file `sales_data.db` is in the `data/` folder.
2. Write your SQL query in `sql/query.sql`.
3. Run the main script:

```bash
python sales_analysis.py
```

4. The results will be printed in the terminal, and the chart will be saved in the `charts/` folder.

---

## 📈 Sample SQL Query (`sql/query.sql`)

```sql
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
```


