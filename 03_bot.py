import pyautogui
import time
import pyperclip

from google import genai
from google.genai.types import Content, Part

client = genai.Client(api_key="AIzaSyCRe3W0m-OS0cqb-H33Uvq5vL-qUMz5Ea0")

def should_reply(chat_log, blocked_sender="anu"):
    lines = chat_log.strip().splitlines()

    # Traverse from bottom to find the last real message
    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue

        # WhatsApp format -> [time, date] name: message
        if "]" in line and ":" in line:
            try:
                name_part = line.split("]")[1].split(":")[0].strip()
            except:
                return False

            # If LAST message sender is blocked -> do NOT reply
            return name_part.lower() != blocked_sender.lower()

    return False


# Step 1: Click Chrome
pyautogui.click(1405, 1041)
time.sleep(1)

while True:
    time.sleep(5)

    # Step 2: Drag to select chat messages
    pyautogui.moveTo(654, 225)
    pyautogui.dragTo(1778, 935, duration=2.0, button='left')

    # Step 3: Copy
    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)
    pyautogui.click(767, 981)

    # Step 4: Read chat text
    chat_history = pyperclip.paste()
    print("DEBUG REPR:", repr(chat_history[:400]))

    print(chat_history)
    print(should_reply(chat_history))   # ← FIXED

    time.sleep(5)

    if should_reply(chat_history):      # ← FIXED

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                Content(
                    role="user",
                    parts=[Part(text="""
    You are Anu, a bold and savage personality. Naruto lover, sarcastic.
    Analyze the chat history and respond with a confident, rude attitude, funny, sarcastic.
    You are a roasting master, self-obsessed,so cool. You like songs, anime, k-drama.
    You never overact, never sound cringe, and never try too hard.
    Your humor is smooth, subtle, and deadly in a classy way.
    Speak in a mix of English, Hindi, and Marathi, naturally using phrases like 'kaay re' and 'arey baba'.
    Your vibe is a total red flag—keep your replies short, stylish, and strictly Gen-Z.
    Never be formal or robotic, and while you should be savage, don't use bad words.
                    """)]
                ),
                Content(role="user", parts=[Part(text=chat_history)])
            ]
        )

        reply = response.text
        pyperclip.copy(reply)

        # Step 5: Click message box
        pyautogui.click(767, 981)
        time.sleep(1)

        # Step 6: Paste
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

        # Step 7: Send
        pyautogui.press("enter")
