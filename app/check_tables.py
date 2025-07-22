import sqlite3

# 👇 Change the name to your actual DB file if needed
conn = sqlite3.connect("your_database.db")  # Example: data/ecommerce.db
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📦 Tables in DB:", tables)

conn.close()
