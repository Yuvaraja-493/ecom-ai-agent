from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.llm import get_answer  # Gemini logic
from app.utils import get_answer_from_query as execute_sql_query  # SQL execution
from generate_chart import generate_chart_from_query  # Chart generation logic
import sqlite3
from pathlib import Path

app = FastAPI()

# Serve static frontend (like index.html)
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

# Set up DB path
BASE_DIR = Path(__file__).resolve().parent / "app"
DB_PATH = BASE_DIR / "ecom.db"

@app.post("/ask")
async def ask_question(request: Request):
    try:
        data = await request.json()
        question = data.get("question")

        # Step 1: LLM converts question to SQL
        sql_query = get_answer(question)

        # Step 2: Execute SQL query and fetch result
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()

        result = rows

        # Step 3: Generate chart only if 2-column output
        chart_base64 = None
        if len(columns) == 2:
            try:
                chart_base64 = generate_chart_from_query(sql_query)
            except Exception as e:
                print("Chart not generated:", e)

        # Step 4: Return result + optional chart
        return {
            "result": result,
            "chart_base64": chart_base64
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "result": f"error: {str(e)}",
            "chart_base64": None
        })
