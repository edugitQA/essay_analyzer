def adaptar_feedback(analise, banca):
    feedback = f"Análise da redação para a banca '{banca}':\n\n"
    
    for resultado in analise:
        # Iterar sobre os itens da lista em 'resultado'
        for item in resultado:
            label = item['label']
            score = item['score']
            feedback += f"Criterio: {label}\nScore: {score}\n\n"

    feedback += "Sugestões de melhorias:\n"
    feedback += "- Revise a estrutura do texto para garantir um fluxo coerente.\n"
    feedback += "- Adeque a linguagem ao tema proposto pela banca.\n"
    feedback += "- Certifique-se de que o conteúdo está bem desenvolvido e cobre todos os pontos necessários.\n"
    feedback += "- Trabalhe na coesão e coerência do texto.\n"
    
    return feedback
