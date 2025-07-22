import sqlite3
import pandas as pd
import os

def load_excel_to_sqlite():
    # Absolute paths
    base_dir = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(base_dir, '..', 'data')
    db_dir = os.path.join(base_dir, '..', 'db')
    os.makedirs(db_dir, exist_ok=True)

    db_path = os.path.join(db_dir, 'ecommerce.db')

    # Paths to actual .xlsx files
    files = {
        "ad_sales": os.path.join(data_dir, "ad_sales.xlsx"),
        "total_sales": os.path.join(data_dir, "total_sales.xlsx"),
        "eligibility": os.path.join(data_dir, "eligibility.xlsx")
    }

    # Check file existence before proceeding
    for name, path in files.items():
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ File not found: {path}")

    # Connect to SQLite DB
    conn = sqlite3.connect(db_path)

    # Read and insert each Excel file
    for table_name, excel_path in files.items():
        df = pd.read_excel(excel_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"✅ Loaded '{table_name}' into database")

    conn.close()
    print("🎉 All Excel files loaded into ecommerce.db")

if __name__ == "__main__":
    load_excel_to_sqlite()
