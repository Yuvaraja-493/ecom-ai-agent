import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyBt1lMnetBlm1ynkYTUhyGRU0BBnyD7vZs")  # ideally use .env

# Choose the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_answer(question: str) -> str:
    prompt = f"""
You are an expert SQL assistant. Convert the following natural language question into a valid SQLite query.
The database has one table named `products` with the following columns:

- id INTEGER
- name TEXT
- category TEXT
- price REAL
- stock INTEGER
- sales INTEGER
- revenue REAL (if not available, assume revenue = price * sales)

Only return a valid SQLite SQL query.
Do not include explanations, markdown, or backticks.
If asked for revenue, always use COALESCE(revenue, price * sales) as revenue
Use aliases like `AS` where helpful.
If aggregation is required, use SUM().
If a group is requested, use GROUP BY.
If sorting is implied, use ORDER BY.

Question: {question}
"""
    response = model.generate_content(prompt)
    sql = response.candidates[0].content.parts[0].text.strip()
    print("🔵 Gemini SQL Response:\n", sql)
    return sql
