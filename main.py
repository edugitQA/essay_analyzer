import tkinter as tk
from tkinter import filedialog
from modules import data_reader, ai_analyzer

def selecionar_arquivo():
    global caminho_arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecionar Arquivo", filetypes=[("Arquivos de Texto", "*.txt"), ("Documentos Word", "*.docx")]
    )
    if caminho_arquivo:
        arquivo_label.config(text=f"Arquivo selecionado: {caminho_arquivo}")
    else:
        arquivo_label.config(text="Nenhum arquivo selecionado")

def analisar_redacao():
    if not caminho_arquivo:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro: Nenhum arquivo selecionado.\n")
        return
    
    texto = data_reader.ler_arquivos(caminho_arquivo)
    if not texto or not texto.strip():
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro: O arquivo está vazio ou não pôde ser lido.\n")
        return
    
    banca = entrada_banca.get()
    if not banca:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro: Nenhuma banca especificada.\n")
        return

    feedback = ai_analyzer.analisar(texto, banca)

    if feedback is None:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro na análise de texto.\n")
        return

    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, feedback)

# Inicialização da interface gráfica
root = tk.Tk()
root.title("Analisador de Redações")

# Entrada para especificação da banca examinadora
tk.Label(root, text="Informe a Banca Examinadora:").pack(pady=5)
entrada_banca = tk.Entry(root)
entrada_banca.pack(pady=5)

# Botão para seleção de arquivo
botao_arquivo = tk.Button(root, text="Selecionar o Arquivo", command=selecionar_arquivo)
botao_arquivo.pack(pady=10)

# Label para exibir o arquivo selecionado
arquivo_label = tk.Label(root, text="Nenhum arquivo selecionado")
arquivo_label.pack(pady=5)

# Área de texto para exibição do resultado
resultado_text = tk.Text(root, wrap=tk.WORD)
resultado_text.pack(pady=10)

# Botão Start
botao_start = tk.Button(root, text="Analisar", command=analisar_redacao)
botao_start.pack(pady=10)

# Loop principal da interface gráfica
root.mainloop()
