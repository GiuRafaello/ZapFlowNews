import os
import psycopg2
import json
from dotenv import load_dotenv
from datetime import datetime, date
from decimal import Decimal

# Carregar variáveis de ambiente do .env
load_dotenv()

# Função para conectar ao banco PostgreSQL
def conectar_db():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            database=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS")
        )
        return conn
    except Exception as e:
        print("Erro ao conectar no banco:", e)
        raise

# Função para carregar dados da tabela gold_vendas_por_produto
def carregar_dados_gold_vendas_por_produto():
    conn = conectar_db()
    query = "SELECT * FROM gold_vendas_por_produto;"
    with conn.cursor() as cursor:
        cursor.execute(query)
        dados = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
    dados_dict = [dict(zip(colunas, row)) for row in dados]
    conn.close()
    return dados_dict

# Função para carregar dados da tabela gold_vendas_por_vendedor
def carregar_dados_gold_vendas_por_vendedor():
    conn = conectar_db()
    query = "SELECT * FROM gold_vendas_por_vendedor;"
    with conn.cursor() as cursor:
        cursor.execute(query)
        dados = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
    dados_dict = [dict(zip(colunas, row)) for row in dados]
    conn.close()
    return dados_dict

# Função para serializar tipos não nativos do JSON
def custom_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Tipo {type(obj)} não é serializável")

# Função para salvar dados em arquivo JSON
def salvar_em_json(dados, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4, default=custom_serializer, ensure_ascii=False)

# Execução principal
if __name__ == "__main__":
    try:
        print("Conectando ao banco...")
        conn = conectar_db()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1;")
            print("Conexão bem-sucedida!")
        conn.close()

        print("Carregando dados de gold_vendas_por_vendedor...")
        dados_vendas_por_vendedor = carregar_dados_gold_vendas_por_vendedor()
        salvar_em_json(dados_vendas_por_vendedor, "gold_vendas_por_vendedor.json")

        print("Carregando dados de gold_vendas_por_produto...")
        dados_gold_vendas_por_produto = carregar_dados_gold_vendas_por_produto()
        salvar_em_json(dados_gold_vendas_por_produto, "gold_vendas_por_produto.json")

        print("✅ Dados salvos com sucesso em 'gold_vendas_por_vendedor.json' e 'gold_vendas_por_produto.json'.")
    except Exception as erro:
        print("❌ Falha na execução:", erro)
