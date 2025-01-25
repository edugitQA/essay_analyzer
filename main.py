from app.file_processor import process_file
from app.text_analyzer import analyze_text
from app.feedback_generator import generate_feedback

def main():
    print("Bem-vindo ao Analisador de Redações!")
    file_path = input("Insira o caminho do arquivo (.txt ou .docx): ")

    try:
        # Processar o arquivo
        original_text = process_file(file_path)

        # Analisar o texto com a API Hugging Face
        analyzed_text = analyze_text(original_text)

        # Gerar feedback
        feedback = generate_feedback(original_text, analyzed_text)

        # Exibir o feedback
        print("\n" + feedback)

        # Salvar o feedback em um arquivo
        output_path = "feedback_redacao.txt"
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(feedback)
        print(f"\nFeedback salvo em: {output_path}")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
