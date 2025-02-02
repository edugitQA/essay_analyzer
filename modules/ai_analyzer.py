from transformers import pipeline

def analisar(texto):
    nlp = pipeline("text-classification", model="bert-base-uncased")
    return nlp(texto)