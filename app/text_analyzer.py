import os
from transformers import pipeline
import os
from dotenv import load_dotenv




# Carregar variáveis de ambiente
load_dotenv()

# Obter o token da API Hugging Face
huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

# Configurar o pipeline da API
pipe = pipeline("text2text-generation", model="facebook/bart-large-cnn", use_auth_token=huggingface_token)

def analyze_text(text):
    try:
        result = pipe(text, max_length=500, min_length=100, do_sample=False)
        return result[0]['generated_text']
    except Exception as e:
        return f"Erro ao analisar o texto: {e}"



