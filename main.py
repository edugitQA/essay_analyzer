import tkinter as tk 
from tkinter import filedialog
from modules import data_reader, ai_analyzer, corrector, scorer, feedback_adapter


def analisar_redacao():
    caminho_arquivo = filedialog.askopenfilename(
        title="selecionar Arquivo", filetypes=[("Arquivos de Texto", "*.txt"), ("Documentos Word", "*.docx")]
    )
    if caminho_arquivo:
        texto = data_reader.ler_arquivos(caminho_arquivo)
        banca = entrada_banca.get()
        analise = ai_analyzer.analisar(texto)

        correcoes = corrector.corrigir(analise)

        pontuacao = scorer.calcular_pontuacao(analise, banca)

        feedback = feedback_adapter.adapter_feedback(correcoes, banca)

        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, f"Pontuação: {pontuacao}\n\n")
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
