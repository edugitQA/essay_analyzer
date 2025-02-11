from docx import Document
from google.cloud import vision

def ler_arquivos(caminho_arquivo):
    if caminho_arquivo.endswith(".txt"):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                return arquivo.read()
        except Exception as e:
            print(f"Erro ao ler o arquivo .txt: {e}")
            return ""
    elif caminho_arquivo.endswith(".docx"):
        try:
            document = Document(caminho_arquivo)
            texto = ""
            for paragraph in document.paragraphs:
                texto += paragraph.text + "\n"
            return texto
        except Exception as e:
            print(f"Erro ao ler o arquivo .docx: {e}")
            return ""
    else:
        print("Formato de arquivo não suportado.")
        return ""

def ler_texto_da_imagem(caminho_para_imagem):
    client = vision.ImageAnnotatorClient()
    with open(caminho_para_imagem, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    text = ""
    for annotation in response.text_annotations:
        text += annotation.description
    return text
