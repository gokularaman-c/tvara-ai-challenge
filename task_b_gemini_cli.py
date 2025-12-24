import sys
import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY not set")
    sys.exit(1)

prompt = sys.argv[1] if len(sys.argv) > 1 else "Hello Gemini"

url = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.0-flash:generateContent"
)

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [{"text": prompt}]
        }
    ]
}

response = requests.post(
    f"{url}?key={API_KEY}",
    headers=headers,
    json=data
)

result = response.json()

try:
    print(result["candidates"][0]["content"]["parts"][0]["text"])
except Exception:
    print("Error response:")
    print(result)
