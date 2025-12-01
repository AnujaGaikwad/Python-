from google import genai

client = genai.Client(api_key= "AIzaSyB4n0r6sJhx-BQCFMjcuzldKhojNtblRV8")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        {
            "role": "user",
            "parts": [
                {"text": "You are Jarvis, a helpful AI assistant. What is coding?"}
            ]
        }
    ]
)

print("Jarvis:", response.text)
