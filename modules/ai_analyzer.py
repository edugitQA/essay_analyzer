from transformers import pipeline
import torch

def analisar(texto):
    nlp = pipeline("text-classification", model="bert-base-uncased")
    return nlp(texto, truncation=True)  # Add truncation=Trueo texto diretamente como argumento posicional
