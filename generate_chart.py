import sqlite3
import matplotlib.pyplot as plt
import io
import base64
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = (Path(__file__).resolve().parent / "app" / "ecom.db").resolve()
conn = sqlite3.connect(DB_PATH)

def generate_chart_from_query(query: str) -> str:
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    if len(columns) != 2:
        raise Exception("Chart generation expects 2 columns: label and value")

    labels = [str(row[0]) for row in rows]
    values = [row[1] for row in rows]

    # Bright color palette (auto-shuffled)
    color_palette = [
        '#FF6B6B', '#4ECDC4', '#556270', '#C7F464', '#FFA07A',
        '#FFB347', '#FFD700', '#B19CD9', '#87CEFA', '#90EE90'
    ]
    random.shuffle(color_palette)

    # Plot
    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, values, color=color_palette[:len(labels)])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:,.0f}',
                 ha='center', va='bottom', fontsize=10)

    plt.xlabel(columns[0], fontsize=12)
    plt.ylabel(columns[1], fontsize=12)
    plt.title(f"{columns[1]} by {columns[0]}", fontsize=14, fontweight='bold')
    plt.xticks(rotation=15)
    plt.tight_layout()

    # Save to base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150)
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')
