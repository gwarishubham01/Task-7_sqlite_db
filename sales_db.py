import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to SQLite database (or create one)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Step 2: Creating sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        product TEXT,
        quantity_sold INTEGER,
        price_per_unit REAL
    )
''')

# Insert sample data
sample_data = [
    ('Product A', 10, 15.0),
    ('Product B', 20, 25.0),
    ('Product C', 5, 30.0),
    ('Product A', 7, 15.0),
    ('Product B', 3, 25.0)
]

cursor.executemany('INSERT INTO sales VALUES (?, ?, ?)', sample_data)
conn.commit()

# Step 3: Run SQL query to get total quantity sold and total revenue per product
query = '''
SELECT 
    product, 
    SUM(quantity_sold) AS total_quantity,
    SUM(quantity_sold * price_per_unit) AS total_revenue
FROM sales
GROUP BY product    
'''

df = pd.read_sql_query(query, conn)

# Step 4: Print the results
print("Sales Summary:")
print(df)

# Step 5: Visualize with bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['product'], df['total_quantity'], color='skyblue', label='Total Quantity')
plt.bar(df['product'], df['total_revenue'], color='orange', alpha=0.6, label='Total Revenue')
plt.xlabel('Product')
plt.title('Total Quantity & Revenue per Product')
plt.legend()
plt.tight_layout()
#plt.savefig("sales_chart.png")
plt.show()




# Close connection
conn.close()
