import sqlite3

# 👇 Change the name to your actual DB file if needed
conn = sqlite3.connect("app/ecom.db")
  # Example: data/ecommerce.db
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📦 Tables in DB:", tables)
for table_name in tables:
    print(f"\n📄 Schema for table: {table_name[0]}")
    cursor.execute(f"PRAGMA table_info({table_name[0]});")
    for row in cursor.fetchall():
        print(row)


conn.close()
