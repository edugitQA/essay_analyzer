from docx import Document

def ler_arquivos(caminho_arquivo):
    if caminho_arquivo.endswith(".text"):
        with open(caminho_arquivo, "r", encoding="utf-8") as Arquivo:
            return arquivo.read()
    elif caminho_arquivo.endswith(".docx"):
        document = Document(caminho_arquivo)
        texto = ""
        for paragraph in document.paragraphs:
            texto += paragraph.text + "\n"
        return texto