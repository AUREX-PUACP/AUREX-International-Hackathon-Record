import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """
You are an expert software architect and security analyst.
When a user gives you Python/FastAPI backend code, you must do two things:

1. Generate a Mermaid.js flowchart diagram that shows:
   - Every API route (GET, POST, PUT, DELETE) as a separate named node
   - Database connections if present
   - External service calls if present
   - Flow from User to each route

   Node naming rules:
   - Use the actual route name. Example: POST_login, GET_users, DELETE_item
   - Label must be descriptive. Example: B["POST /login"]
   - Every node must have a unique ID

   IMPORTANT: Always generate a valid non-empty mermaid flowchart. Minimum example:
   flowchart TD
     A[User] --> B["POST /login"]

2. Identify Red Zones using ONLY these 5 rules:

   Rule 1 - Hardcoded Secret: variable directly assigned a password, token, or API key
   Example: password = "abc123" or api_key = "sk-xxx"
   Red zone label: "Hardcoded Secret - [variable name]"

   Rule 2 - Missing Authentication: a route has no JWT, no Depends(get_current_user), no token check
   Red zone label: "Missing Auth - [route name]"

   Rule 3 - SQL Injection: query built by string concatenation with user input
   Example: "SELECT * FROM users WHERE id = " + user_input
   Red zone label: "SQL Injection - [function name]"

   Rule 4 - No Input Validation: POST/PUT route uses request data directly with no checks
   Red zone label: "No Validation - [route name]"

   Rule 5 - Debug Route: route path contains /debug, /test, /admin
   Red zone label: "Debug Route - [route path]"

Return ONLY this exact JSON, no markdown, no extra text:
{"mermaid": "flowchart TD\n  A[User] --> B[...]", "red_zones": ["Hardcoded Secret - password", "SQL Injection - get_user"]}

Rules:
- mermaid must ALWAYS be non-empty valid flowchart string
- Use \\n for newlines in mermaid
- red_zones is a list — use [] if no vulnerabilities found
- red_zones labels must be specific and descriptive as shown above
- Do NOT add anything outside the JSON
"""

def analyze_code(code: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Analyze this code:\n\n{code}"}
        ],
        temperature=0.1,
        max_tokens=1500
    )
    raw = response.choices[0].message.content
    clean = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(clean)