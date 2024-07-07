from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    question = input("User: ")

    if question.lower() != "bye":
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=50,
            n=1,
            temperature=0.5  # Adjust temperature as needed
        )

        for choice in response["choices"]:
            print(f"AI: {choice['message']['content']}")
    else:
        print("AI: Bye...")
        break
