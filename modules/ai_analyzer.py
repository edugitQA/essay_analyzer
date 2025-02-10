import requests
from config import HUGGINGFACE_API_KEY

def analisar(texto, banca):
    prompt = f"Você é um especialista em redação de concursos da banca {banca}. Analise a seguinte redação e forneça feedback detalhado em português para o candidato:\n\nRedação:\n{texto}\n\nFeedback:\n"
    
    headers = {
        'Authorization': f'Bearer {HUGGINGFACE_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'inputs': prompt,
        'parameters': {
            'max_length': 500,
            'temperature': 0.7
        }
    }
    
    response = requests.post('https://api-inference.huggingface.co/models/EleutherAI/gpt-neox-20b', headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()[0]['generated_text'].strip()
    else:
        print(f"Erro na API: {response.status_code}")
        print(f"Resposta da API: {response.text}")
        return None
