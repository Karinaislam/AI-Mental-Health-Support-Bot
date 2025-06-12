from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


client = OpenAI()

def generate_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a warm, caring mental health companion. Always be empathetic, calm, and encouraging."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.8,
        max_tokens=100
    )
    return response.choices[0].message.content