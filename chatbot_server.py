from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# ATENÇÃO: Se o nome do arquivo é chatbot_server.py, a variável Flask deve ser 'app'
# e o Procfile deve ser: web: gunicorn chatbot_server:app
app = Flask(__name__)
# O CORS é essencial para permitir a comunicação entre seu HTML e o servidor Python
CORS(app) 

# URL base que será usada para as imagens. 
# ATUALIZE ESTA URL quando você hospedar suas imagens no GitHub Pages!
BASE_IMAGE_URL = "https://via.placeholder.com/300x150?text=" 

# --- Base de Conhecimento Expandida ---
FAQ_M365 = {
    "login_computador": {
        "keywords": ["acesso", "login", "entrar", "acessar pc", "computador", "primeiro acesso"],
        "text": f"""
                    🎓 **Acesso ao Computador – Alunos e Professores Senac Camaquã**
                    * **Entrar com Novo Usuário:** Clique em "Novo Usuário" na tela inicial.
                    * **E-mail:** SeuCPF@senacrs.edu.br (Ex: 12345678910@senacrs.edu.br)
                    * **Senha:** Sua Data de Nascimento no formato DDMMAAAA + #Educ (Ex: 30032020#Educ)
                    
                    🔐 *Obs: Senha padrão só funciona se nunca foi alterada. Em caso de problemas ou esquecimento, procure o **Rodrigo na Secretaria**.*
                    """,
        "image_url": f"{BASE_IMAGE_URL}Tela+de+Login" 
    },
    "login_visitante": {
        "keywords": ["visitante", "convidado", "acesso especial", "wifi"],
        "text": f"""
                    🧑‍💼 **Acesso Visitantes:**
                    * **Login:** camaqua01@senacrs.edu.br
                    * **Senha:** Escola.Senac.01
                    
                    * **Rede Wi-Fi Visitantes:** Senac Visitantes
                    * **Senha Wi-Fi:** trijuntos
                    """,
        "image_url": f"{BASE_IMAGE_URL}Login+Visitante"
    },
    "ativar_office": {
        "keywords": ["ativar office", "word", "excel", "powerpoint", "licença office"],
        "text": f"""
                    ✅ **Ativar o Pacote Office**
                    1.  **Abra** qualquer aplicativo Office (Word, Excel). Uma janela de login irá se abrir.
                    2.  Clique em **'Entrar ou Criar uma conta'**.
                    3.  **Insira seu e-mail** (SeuCPF@senacrs.edu.br) e **sua senha** (a mesma do login do computador).
                    4.  Se solicitado, realize a **troca de senha** (insira a atual, a nova e confirme).
                    5.  Na tela de “Aceitar o contrato de licença”, clique em **“Aceitar”**.
                    6.  Pronto, Office ativado!
                    """,
        "image_url": f"{BASE_IMAGE_URL}Ativar+Office"
    },
    "portal_aluno_acesso": {
        "keywords": ["portal do aluno", "acessar portal", "login portal"],
        "text": f"""
                    💻 **Acessar o Portal do Aluno**
                    1.  Acesse o site do Senac-RS: [clique aqui](https://www.senacrs.com.br/)
                    2.  Clique no ícone de usuário (menu superior à direita) e escolha **"Portal do Aluno"**.
                    3.  **Login:** Seu CPF ou Matrícula.
                    4.  **Senha:** Sua Data de Nascimento no formato DDMMAAAA (ou a senha atual).
                    
                    *Obs: Na primeira vez, o sistema pedirá para você trocar a senha (as mesmas regras de senha forte se aplicam). Em caso de esquecimento, procure a Hellen ou o Rodrigo na Secretaria.*
                    """,
        "image_url": f"{BASE_IMAGE_URL}Portal+Aluno+Login"
    },
    "solicitar_servico": {
        "keywords": ["solicitar serviço", "justificativa", "atestado escolar", "protocolo"],
        "text": f"""
                    📄 **Solicitar Serviço/Protocolo (Portal do Aluno)**
                    1.  **Acesse o Portal do Aluno** (veja o tópico 'portal do aluno' se precisar).
                    2.  Selecione **"Ambiente do Estudante"**.
                    3.  No menu à esquerda, selecione **"Autoatendimento"** > **"Solicitar Serviço"** (botão laranja).
                    4.  Escolha o serviço desejado (Ex: "Justificativa de Faltas").
                    5.  Preencha os campos (Matrícula, Observações) e **Anexe o arquivo** (atestado, etc.).
                    6.  Verifique e clique em **Enviar** duas vezes.
                    """,
        "image_url": f"{BASE_IMAGE_URL}Solicitar+Servico"
    },
    "justificativa_falta": {
        "keywords": ["justificar falta", "atestado medico", "atraso justificativa"],
        "text": f"""
                    📅 **Justificativa de Faltas**
                    * **Documentos:** Devem ser amparados por documentos legais (atestado médico, convocação, etc.).
                    * **Prazo:** O atestado deve ser lançado no máximo **até 2 dias úteis** no Portal do Aluno.
                    * **Como Lançar:** Siga o passo a passo de 'solicitar serviço' no portal do aluno.
                    """,
        "image_url": "" 
    },
    "trocar_senha_computador": {
        "keywords": ["trocar senha computador", "alterar senha pc", "senha forte"],
        "text": f"""
                    🔑 **Troca de Senha do Computador/Rede**
                    1.  Aperte as teclas **Ctrl + Alt + Delete**.
                    2.  Clique em **"Alterar uma senha"**.
                    3.  Preencha: "Senha Atual", "Nova Senha" e "Confirmar Nova Senha".
                    
                    **Dicas de Senha Forte:** Mínimo de 8 caracteres, com letras maiúsculas, minúsculas, números e caracteres especiais.
                    """,
        "image_url": f"{BASE_IMAGE_URL}CtrlAltDel"
    },
    "biblioteca_online": {
        "keywords": ["biblioteca online", "livros digitais", "pergamum"],
        "text": f"""
                    📚 **Acesso à Biblioteca Online (Minha Biblioteca)**
                    1.  Acesse o Site do Senac-RS e vá em **"Bibliotecas"**.
                    2.  Role até encontrar o logo **"Minha Biblioteca"**.
                    3.  Insira seu login e senha do Pergamum (se ainda não tiver, solicite na Secretaria).
                    
                    *O portal oferece acesso a mais de 11 mil livros digitais.*
                    """,
        "image_url": f"{BASE_IMAGE_URL}Biblioteca+Online"
    },
    "emprestimo_livros": {
        "keywords": ["emprestimo livro", "renovacao", "multa biblioteca"],
        "text": f"""
                    📖 **Empréstimo de Livros – Biblioteca Física**
                    * **Empréstimo:** Escolha o livro na área de convivência e leve-o à Secretaria para registro.
                    * **Prazo:** 7 dias corridos.
                    * **Renovação:** É possível solicitar renovação por +7 dias, mas o pedido deve ser feito **dentro do prazo inicial**.
                    * **Multa:** R$ 1,00 para cada dia de atraso.
                    """,
        "image_url": ""
    },
    "cursos": {
        "keywords": ["cursos", "cursos livres", "cursos tecnicos", "ead", "graduação"],
        "text": f"""
                    🎓 **Conheça Nossas Áreas de Cursos!**
                    * **FIC e Livres:** [senacrs.com.br/cursosLivres](https://www.senacrs.com.br/cursosLivres)
                    * **Técnicos:** [senacrs.com.br/cursosTecnicos](https://www.senacrs.com.br/cursosTecnicos)
                    * **EAD (FIC, Técnico, Pós):** [ead.senac.br/niveis-de-ensino/](https://www.ead.senac.br/niveis-de-ensino/)
                    
                    *Para visualizar vagas, selecione **Senac Camaquã** na plataforma.*
                    """,
        "image_url": f"{BASE_IMAGE_URL}Cursos"
    },
    "contatos_cursos": {
        "keywords": ["whatsapp", "consultoras", "contato cursos"],
        "text": f"""
                    📞 **Contatos das Consultoras de Cursos:**
                    * **Laurielle:** [clique para falar](https://api.whatsapp.com/send/?phone=5551999160202&text&type=phone_number&app_absent=0)
                    * **Thais:** [clique para falar](https://api.whatsapp.com/send/?phone=5551985942119&text&type=phone_number&app_absent=0)
                    * **Tailine:** [clique para falar](https://api.whatsapp.com/send/?phone=5551991246334&text&type=phone_number&app_absent=0)
                    """,
        "image_url": ""
    },
    "contato_secretaria": {
        "keywords": ["falar com secretaria", "contato secretaria"],
        "text": f"""
                    💬 **Contato da Secretaria (WhatsApp):**
                    * [Clique para falar com a Secretaria](https://api.whatsapp.com/send/?phone=5551992680906&text&type=phone_number&app_absent=0)
                    """,
        "image_url": ""
    },
    "documentos_entrega": {
        "keywords": ["certificado", "diploma", "atestado de matricula", "prazo"],
        "text": f"""
                    📄 **Certificados, Diplomas e Atestados**
                    * **Certificado/Diploma:** Requeridos em 10 dias úteis após o protocolo **E** o professor fechar todos os diários de turma.
                    * **Atestado de Matrícula Padrão:** Retire diretamente pelo Portal do Aluno (Ambiente do Estudante > Página Principal > Atestado de Matrícula).
                    * **Atestado Customizado:** Abra um protocolo (veja 'solicitar serviço') solicitando e descrevendo o que precisa nas observações (prazo: 6 dias úteis).
                    """,
        "image_url": f"{BASE_IMAGE_URL}Atestado+Matricula"
    },
    "pagamentos": {
        "keywords": ["pagar curso", "boleto", "pix", "cartao", "financeiro", "pagar"],
        "text": f"""
                    💰 **Pagamento de Cursos**
                    * **Portal do Aluno:** No menu, selecione **Página Principal** > **Financeiro**. Marque as alternativas e escolha pagar por Boleto, Pix ou Cartão de Crédito.
                    * **Presencial:** No setor financeiro da escola, procure pelo **Tainã** ou **Tatiane**.
                    * **WhatsApp Financeiro:** [Clique aqui](https://api.whatsapp.com/send/?phone=5551991701052&text&type=phone_number&app_absent=0)
                    """,
        "image_url": f"{BASE_IMAGE_URL}Financeiro+Portal"
    },
    "boletim": {
        "keywords": ["boletim", "notas", "ver nota"],
        "text": f"""
                    📊 **Acesso ao Boletim**
                    1.  **Acesse o Portal do Aluno** (veja o tópico 'portal do aluno' se precisar).
                    2.  No menu à direita, escolha a opção **"Boletim"**.
                    3.  Selecione seu curso e as notas aparecerão.
                    """,
        "image_url": f"{BASE_IMAGE_URL}Boletim"
    },
    "cursos_gratuitos": {
        "keywords": ["psg", "gratuitos", "vagas gratuitas", "inscrever cursos"],
        "text": f"""
                    🆓 **Cursos Gratuitos (PSG)**
                    * Acesse: [www.senacrs.com.br/hotsite/psg/partials/vagas-filter.php](www.senacrs.com.br/hotsite/psg/partials/vagas-filter.php)
                    * Use a busca para encontrar vagas em Camaquã, confira os requisitos e inscreva-se para concorrer.
                    """,
        "image_url": ""
    },
    "trabalhe_conosco": {
        "keywords": ["trabalhe conosco", "vagas emprego", "oportunidades trabalho"],
        "text": f"""
                    💼 **Trabalhe Conosco (Vagas Senac)**
                    * Acesse: [www.trabalhenosistema.com.br](www.trabalhenosistema.com.br)
                    * Faça login, cadastre seus dados e acompanhe as vagas disponíveis no site e nas redes sociais do Senac Camaquã.
                    """,
        "image_url": ""
    }
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
                    # Tratamento extra para quebra de linha com HTML e negrito
                    "text": data["text"],
                    "image_url": data.get("image_url", "")
                }
            
    # Resposta Padrão/Fallback se nenhuma palavra-chave for encontrada
    return {
        "text": "Desculpe, não encontrei uma resposta para sua pergunta sobre o Senac Camaquã. Tente usar palavras-chave como 'login', 'senha', 'portal do aluno' ou 'cursos'.",
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