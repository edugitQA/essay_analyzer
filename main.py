import tkinter as tk
from tkinter import filedialog
from modules import data_reader, ai_analyzer

def analisar_redacao():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecionar Arquivo", filetypes=[("Arquivos de Texto", "*.txt"), ("Documentos Word", "*.docx")]
    )
    if caminho_arquivo:
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

root = tk.Tk()
root.title("Analisador de Redações")

botao_arquivo = tk.Button(root, text="Selecionar o Arquivo", command=analisar_redacao)
botao_arquivo.pack(pady=10)

entrada_banca = tk.Entry(root)
entrada_banca.pack(pady=5)

resultado_text = tk.Text(root, wrap=tk.WORD)
resultado_text.pack()

root.mainloop()


