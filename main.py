from fastapi import FastAPI, Request
import sqlite3
from app.llm import query_gemini

app = FastAPI()

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "")

    try:
        sql = query_gemini(question)

        # Connect to your database
        conn = sqlite3.connect("ecom.db")
        cursor = conn.cursor()

        # Execute the generated SQL
        cursor.execute(sql)
        rows = cursor.fetchall()

        return {"result": rows}
    
    except Exception as e:
        print("❌ Failed SQL:\n", sql)
        print("⚠️ Error:", str(e))
        return {"error": "Invalid SQL returned by LLM"}
