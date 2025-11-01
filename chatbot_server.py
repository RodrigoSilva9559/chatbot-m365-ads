from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# O CORS é essencial para permitir a comunicação entre seu HTML local e o servidor Python
CORS(app) 

# --- Base de Conhecimento com Texto e Imagem ---
# ATENÇÃO: Use links de placeholder até ter seus prints reais. 
# Quando hospedar, você precisará atualizar estes links.
FAQ_M365 = {
    "login": {
        "keywords": ["acesso", "login", "entrar", "acessar pc", "computador"],
        "text": """
                    🎓 Acesso ao Computador – Alunos e Professores Senac Camaquã
                    Na tela inicial, clique em "Novo Usuário".
                    E-mail: Digite seu CPF seguido de @senacrs.edu.br. (Ex: 12345678910@senacrs.edu.br)
                    Senha: Digite sua data de nascimento no formato DDMMAAAA seguida de #Educ. (Ex: 30032020#Educ)
                    🔐 Importante: Essa senha padrão só funciona se você nunca alterou.
                    """,
        "image_url": "https://via.placeholder.com/300x150?text=Tela+de+Login" 
    },
    "visitante": {
        "keywords": ["visitante", "convidado", "acesso especial"],
        "text": """
                    🧑‍💼 Acesso Visitantes:
                    Login: camaqua01@senacrs.edu.br
                    Senha: Escola.Senac.01
                    Por favor, utilize este acesso apenas para fins de demonstração ou trabalho de curto prazo.
                    """,
        "image_url": "https://via.placeholder.com/300x150?text=Login+Visitante"
    },
    "teams": {
        "keywords": ["teams", "reuniao", "aula online", "chamar"],
        "text": "O Microsoft Teams é usado para comunicação, reuniões e aulas online. Você pode acessá-lo diretamente pelo portal do M365 (office.com), após o login.",
        "image_url": "https://via.placeholder.com/300x150?text=Icone+Teams"
    },
    "senha": {
        "keywords": ["senha nao funciona", "mudar senha", "esqueci"],
        "text": "Se sua senha do M365 não funciona ou você precisa resetar, você precisa entrar em contato com o suporte de TI da escola (o Rodrigo na Secretaria).",
        "image_url": "" # Sem imagem para esta resposta
    }
    # Adicione mais tópicos aqui seguindo o mesmo padrão!
}


def get_resposta(pergunta_usuario):
    pergunta_usuario = pergunta_usuario.lower()
    
    # Itera sobre os tópicos na base de conhecimento
    for topico, data in FAQ_M365.items():
        # Itera sobre as palavras-chave do tópico
        for keyword in data["keywords"]:
            if keyword in pergunta_usuario:
                # Retorna a resposta se encontrar uma palavra-chave
                return {
                    "text": data["text"],
                    "image_url": data.get("image_url", "")
                }
            
    # Resposta Padrão/Fallback se nenhuma palavra-chave for encontrada
    return {
        "text": "Desculpe, não encontrei uma resposta para sua pergunta sobre o M365/Senac Camaquã. Tente usar palavras-chave como 'login', 'senha', ou 'teams'.",
        "image_url": ""
    }


@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"text": "Por favor, digite uma pergunta.", "image_url": ""})

    resposta_data = get_resposta(user_query)
    
    # Envia o objeto JSON de resposta (text e image_url)
    return jsonify(resposta_data)


if __name__ == '__main__':
    # Configuração local padrão
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)