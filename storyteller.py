from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def main():
    while True:
        user_input = input("""Make a story about: """)
        if user_input.lower() == "exit":
            break
        
        response = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"Make a story about {user_input}"},
                {"role": "user", "content": user_input}
            ]
        )
        
        print("AI: ", response.choices[0].message.content)
if __name__ == "__main__":    main()
