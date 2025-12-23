import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def pergunte_ao_groq(pergunta: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )
    return response.choices[0].message.content

question = "Quanto eu vendi ontem?"
answer = pergunte_ao_groq(question)

print(f"Resposta do Groq: {answer}")



