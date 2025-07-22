import google.generativeai as genai

# Configure your Gemini API key
genai.configure(api_key="AIzaSyBau4OwNFq07_VAR1xlHhILWNiZed_aCrI")  # Replace or load from .env

# Choose the model
model = genai.GenerativeModel("gemini-1.5-flash")

def query_gemini(question: str) -> str:
    prompt = f"""
You are an expert SQL assistant. Convert the following natural language question into a valid SQLite query.
The database has one table: products with the following columns:

- id INTEGER
- name TEXT
- category TEXT
- price REAL
- stock INTEGER

Only return the SQL query. Do not include explanations, markdown, or backticks.

Question: {question}
"""
    response = model.generate_content(prompt)

    sql = response.candidates[0].content.parts[0].text.strip()
    print("🔵 Gemini SQL Response:\n", sql)
    
    return sql
