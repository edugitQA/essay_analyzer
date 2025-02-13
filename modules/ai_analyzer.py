import requests
from logger_config import   logger
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
        logger.info("Enviando solicitaçõa para API do Gemini")
        response = requests.post(url, json=data)
        response.raise_for_status()
        logger.info("Resposta recebida com sucesso da API")

        response_json = response.json()
        logger.debug("Resposta da API: {response_json}")

        if response_json.get("candidates") and len(response_json["candidates"]) > 0:
            candidate = response_json["candidates"][0]
            if candidate.get("content") and candidate["content"].get("parts"):
                parts = candidate["content"]["parts"]
                feedback = "".join([part.get("text", "") for part in parts]).strip()
                logger.info("Feedback gerado com sucesso pela API do Gemini")
                return feedback
            else:

                locals.error("A resposta da API não continha as chaves 'content' ou 'parts'.")
                logger.debug(f"Resposta JSON: {response_json}")
                return None
        else:
            logger.error("A resposta da API não continha a chave 'candidates' ou estava vazia.")
            logger.debug(f"Resposta JSON: {response_json}")
            return None

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na API do Gemini: {e}")
        if response.status_code != 200:
            logger.error(f"Código de status: {response.status_code}")
            try:
                error_details = response.json()
                logger.error(f"Detalhes do erro: {error_details}")
            except:
                logger.error("Não foi possível decodificar os detalhes do erro.")
        return None

    except (KeyError, IndexError, TypeError) as e:
        logger.error(f"Erro ao processar a resposta da API: {e}")
        try:
            logger.debug(f"Resposta da API: {response_json}")
        except:
            logger.error("Não foi possível imprimir a resposta da API.")
        return None
