import requests
from config import GEMINI_API_KEY

def analisar(texto, banca):
    prompt = f"""Você é um especialista em redação de concursos da banca {banca}. 
    Analise a seguinte redação e forneça feedback detalhado em português para o candidato, 
    incluindo sugestões de melhorias gramaticais, ortográficas, de estilo, coesão e coerência, 
    e uma estimativa da pontuação de acordo com os critérios da banca.

    Redação:
    {texto}

    Feedback:
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()

        response_json = response.json()

        if response_json.get("candidates") and len(response_json["candidates"]) > 0:
            candidate = response_json["candidates"][0]
            if candidate.get("content") and candidate["content"].get("parts"):
                parts = candidate["content"]["parts"]
                feedback = "".join([part.get("text", "") for part in parts]).strip()
                return feedback
            else:
                print("A resposta da API não continha as chaves 'content' ou 'parts'.")
                print(response_json)
                return None
        else:
            print("A resposta da API não continha a chave 'candidates' ou estava vazia.")
            print(response_json)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Erro na API do Gemini: {e}")
        if response.status_code != 200:
            print(f"Código de status: {response.status_code}")
            try:
                error_details = response.json()
                print(f"Detalhes do erro: {error_details}")
            except:
                print("Não foi possível decodificar os detalhes do erro.")
        return None

    except (KeyError, IndexError, TypeError) as e:
        print(f"Erro ao processar a resposta da API: {e}")
        try:
            print(f"Resposta da API: {response_json}")
        except:
            print("Não foi possível imprimir a resposta da API.")
        return None
