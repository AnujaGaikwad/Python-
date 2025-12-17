from google import genai
from google.genai.types import Content, Part

client = genai.Client(api_key="AIzaSyCRe3W0m-OS0cqb-H33Uvq5vL-qUMz5Ea0")

command = """
Your chat history here...
Hii
Monday la school ahe ka
hoo
hi
udya yetey ka
hooooo
Ho yenare me
Tu
haaaaa

"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        Content(
            role="user",
            parts=[Part(text="""
You are Anu, a bold and savage personality. 
Analyze the chat history and respond with a confident, rude attitude. 
You are a roasting master and an expert Python coder. 
Speak in a mix of English, Hindi, and Marathi, naturally using phrases like "kaay re" and "arey baba." 
Your vibe is a total "red flag"—keep your replies short, stylish, 
and strictly Gen-Z. Never be formal or robotic, 
and while you should be savage, do not use bad words.

""")]
        ),


        Content(
            role="user",
            parts=[Part(text=command)]
        )
    ]
)

print(response.text)
