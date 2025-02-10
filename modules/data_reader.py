from docx import Document

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
