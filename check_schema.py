import sqlite3

conn = sqlite3.connect("db/ecommerce.db")
cursor = conn.cursor()

# ✅ Replace this line with your test query
cursor.execute("SELECT * FROM ad_sales WHERE eligibility = 1;")


for row in cursor.fetchall():
    print(row)

conn.close()
