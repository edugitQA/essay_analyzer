def generate_feedback(original_text, analyzed_text):
    feedback = []
    feedback.append("Correções e Melhorias:")
    feedback.append("--------------------------------------------------")
    feedback.append("Texto Original:")
    feedback.append(original_text)
    feedback.append("\nTexto Melhorado:")
    feedback.append(analyzed_text)
    feedback.append("\nSugestões de Estilo e Coesão:")
    feedback.append("- Revise frases longas para maior clareza.")
    feedback.append("- Use conectivos para melhorar a fluidez entre parágrafos.")
    feedback.append("- Evite repetições de palavras próximas.")
    return "\n".join(feedback)
