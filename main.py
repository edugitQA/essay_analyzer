import os
import tkinter as tk
from tkinter import font, filedialog, messagebox, scrolledtext
from logger_config import logger
from modules import data_reader, ai_analyzer
from config import GOOGLE_CLOUD_VISION_KEY

# Defina aqui a sua variável de ambiente para a chave da API do Google Cloud Vision
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_CLOUD_VISION_KEY

def selecionar_arquivo():
    global caminho_arquivo, tipo_arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecionar Arquivo", 
        filetypes=[
            ("Arquivos de Texto", "*.txt"), 
            ("Documentos Word", "*.docx"),
            ("Imagens", "*.png;*.jpg;*.jpeg") 
        ]
    )
    if caminho_arquivo:
        arquivo_label.config(text=f"Arquivo selecionado: {caminho_arquivo}")
        tipo_arquivo = ""
        if caminho_arquivo.endswith(".txt"):
            tipo_arquivo = "txt"
        elif caminho_arquivo.endswith(".docx"):
            tipo_arquivo = "docx"
        elif caminho_arquivo.endswith((".png", ".jpg", ".jpeg")):
            tipo_arquivo = "imagem"
        logger.info(f"Arquivo selecionado: {caminho_arquivo}")
    else:
        arquivo_label.config(text="Nenhum arquivo selecionado")
        tipo_arquivo = ""
        logger.warning("Nenhum arquivo selecionado")

def analisar_redacao():
    global caminho_arquivo, tipo_arquivo
    if not caminho_arquivo:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro: Nenhum arquivo selecionado.\n")
        logger.error("Nenhum arquivo selecionado")
        return

    texto = ""
    if tipo_arquivo == "txt":
        texto = data_reader.ler_arquivos(caminho_arquivo)
    elif tipo_arquivo == "docx":
        texto = data_reader.ler_arquivos(caminho_arquivo)
    elif tipo_arquivo == "imagem":
        try:
            texto = data_reader.ler_texto_da_imagem(caminho_arquivo)
        except Exception as e:
            resultado_text.delete("1.0", tk.END)
            resultado_text.insert(tk.END, f"Erro ao ler imagem: {e}\n")
            logger.error(f"Erro ao ler imagem: {e}")
            return

    if not texto or not texto.strip():
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro: O arquivo está vazio ou não pôde ser lido.\n")
        logger.error("O arquivo está vazio ou não pôde ser lido")
        return

    banca = entrada_banca.get()
    if not banca:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro: Nenhuma banca especificada.\n")
        logger.error("Nenhuma banca especificada")
        return

    feedback = ai_analyzer.analisar(texto, banca)
    if feedback is None:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro na análise de texto.\n")
        logger.error("Erro na análise de texto")
        return

    digitar_texto(resultado_text, feedback)
    logger.info("Análise de redação concluída com sucesso")

def digitar_texto(widget, texto, indice=0):
    if indice < len(texto):
        widget.insert(tk.END, texto[indice])
        widget.after(25, digitar_texto, widget, texto, indice + 1)

def visualizar_logs():
    logs_window = tk.Toplevel(root)
    logs_window.title("Logs")
    logs_window.geometry("600x400")
    logs_text = scrolledtext.ScrolledText(logs_window, wrap=tk.WORD, font=("Times New Roman", 12))
    logs_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    with open('app.log', 'r') as log_file:
        logs_text.insert(tk.END, log_file.read())

root = tk.Tk()
root.title("Analisador de Redações")
root.configure(bg="#f0f0f0")

titulo_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)

frame_banca = tk.Frame(root, bg="#f0f0f0")
frame_banca.pack(pady=10)
tk.Label(frame_banca, text="Informe a Banca Examinadora:", font=label_font, bg="#f0f0f0").pack(side="left")
entrada_banca = tk.Entry(frame_banca)
entrada_banca.pack(side="left", padx=5)

botao_arquivo = tk.Button(root, text="Selecionar o Arquivo", command=selecionar_arquivo,
                          bg="#007acc", fg="#ffffff", relief="flat", padx=10, pady=5)
botao_arquivo.pack(pady=10)

arquivo_label = tk.Label(root, text="Nenhum arquivo selecionado", font=label_font, bg="#f0f0f0")
arquivo_label.pack(pady=5)

resultado_text = tk.Text(root, wrap=tk.WORD, font=("Times New Roman", 12))
resultado_text.pack(pady=10, padx=10)

botao_start = tk.Button(root, text="Analisar", command=analisar_redacao,
                        bg="#28a745", fg="#ffffff", relief="flat", padx=10, pady=5)
botao_start.pack(pady=10)

botao_logs = tk.Button(root, text="Visualizar Logs", command=visualizar_logs,
                       bg="#007acc", fg="#ffffff", relief="flat", padx=10, pady=5)
botao_logs.pack(pady=10)

root.mainloop()
