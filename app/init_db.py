import sqlite3

conn = sqlite3.connect("app/ecom.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS products")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER,
    sales INTEGER,
    revenue REAL
)
""")

# Sample data
sample_data = [
    ("Laptop", "Electronics", 50000, 10, 50, 2500000),
    ("T-Shirt", "Clothing", 500, 200, 100, 50000),
    ("Teddy Bear", "Toys", 300, 150, 75, 22500),
]

cursor.executemany("INSERT INTO products (name, category, price, stock, sales, revenue) VALUES (?, ?, ?, ?, ?, ?)", sample_data)

conn.commit()
conn.close()

print("✅ Database initialized with sample data.")
