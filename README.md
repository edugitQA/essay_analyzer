# Essay Analyzer

Este projeto é uma aplicação em Python para análise e correção de redações utilizando a API do Gemini. A aplicação realiza uma análise completa das redações, fornecendo feedback detalhado e estimativas de pontuação.

## Funcionalidades

- **Análise de Redações:** O sistema recebe um texto de redação e, utilizando a API do Gemini, realiza uma análise completa, identificando erros gramaticais, ortográficos, de estilo, coesão e coerência.
- **Feedback Detalhado:** O sistema gera um feedback detalhado em português, com sugestões de melhorias e explicações sobre os erros encontrados.
- **Estimativa de Pontuação:** Com base na análise, o sistema estima a pontuação da redação de acordo com os critérios da banca examinadora especificada.
- **Interface Gráfica:** O sistema possui uma interface gráfica simples e intuitiva, que permite ao usuário inserir o texto da redação, selecionar a banca examinadora e visualizar o feedback e a pontuação estimada.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - `python-docx`: Para leitura de arquivos .docx
  - `transformers`: Para utilização de modelos de linguagem (caso utilize modelos locais)
  - `python-dotenv`: Para gerenciamento de variáveis de ambiente
  - `requests`: Para requisições HTTP à API do Gemini
  - `google-generativeai`: Para interação com a API do Gemini

## Instalação

Clone o repositório:
      
      git clone https://github.com/edugitQA/essay_analyzer.git

Crie um ambiente virtual:

      python3 -m venv .venv  # Cria o ambiente virtual

Ative o ambiente virtual:
      
      source .venv/bin/activate #linux
      .venv\Scripts\activate #windowns

Instale as dependências:
     
      pip install -r requirements.txt


## Configuração
1. Obtenha uma chave de API do Gemini.
2. Acesse o Google Cloud Console.
3. Crie um projeto ou selecione um projeto existente.
4. Habilite a API do Gemini.
5. Crie credenciais de API da AI que for usar e obtenha sua chave de API.
6. Crie credenciais de API Cloud Vision (Google) e obtenha sua chave de API.

Configure as variáveis de ambiente:
Crie um arquivo .env/config na raiz do projeto:
   
      touch .env ou config.py

Adicione a seguinte linhas ao arquivo .env/config, substituindo SUA_CHAVE_DE_API pela sua chave real:

  
   - `GEMINI_API_KEY=SUA_CHAVE_DE_API`: Para leitura de arquivos .docx
   - `GOOGLE_CLOUD_VISION_KEY:local do json da sua chave API`: Para tratamento de texto de imagens.
    

obs: Fique atento à quantidade de Tokens que sua API disponibiliza gratuitamente.


Execução
Execute o script principal:
     
     python main.py
     
Utilize a interface gráfica:

1. Insira o texto da redação na área de texto.

2. Selecione a banca examinadora no menu dropdown.


3. O feedback detalhado e a pontuação estimada serão exibidos na tela.

Observações
Este projeto utiliza a API do Gemini para análise de texto. Certifique-se de ter uma conexão estável com a internet para que o sistema funcione corretamente.

A qualidade do feedback e da estimativa de pontuação pode variar dependendo do modelo do Gemini utilizado e da qualidade do texto da redação.

Este é um projeto em desenvolvimento. Novas funcionalidades e melhorias podem ser adicionadas no futuro.

## Contribuição
Contribuições são sempre bem-vindas! Se você tiver alguma sugestão, ideia ou encontrar algum problema, por favor, abra uma issue ou envie um pull request.
Espero que este README seja útil! Se você tiver alguma dúvida ou precisar de ajuda adicional, não hesite em perguntar.




