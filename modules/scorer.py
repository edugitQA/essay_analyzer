import json

def calcular_pontuacao(analise, banca):
    with open("data/bancas_examinadoras.json", "r") as arquivo:
        criterios = json.load(arquivo)[banca]

    # Lógica para calcular a pontuação com base nos critérios da banca
    pass