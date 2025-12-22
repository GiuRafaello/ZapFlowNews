import os
from groq import Groq
froimport os
from groq import Groq
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

# Inicializa o cliente Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Função para enviar uma pergunta ao modelo da Groq
def pergunte_ao_groq(pergunta: str):
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",  # ou "llama3-8b-8192", dependendo do modelo que você quer usar
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )
    return response.choices[0].message.content

# Pergunta de exemplo
question = "Quanto eu vendi ontem?"
answer = pergunte_ao_groq(question)

print(f"Resposta do Groq: {answer}")