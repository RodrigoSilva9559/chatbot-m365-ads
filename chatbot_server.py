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
# BASE_IMAGE_URL = "https://via.placeholder.com/300x150?text="
BASE_IMAGE_URL = "https://rodrigosilva9559.github.io/chatbot-m365-ads/imagens/"

# --- Base de Conhecimento Expandida ---
FAQ_M365 = {
    "login_computador": {
        "keywords": ["acesso", "login", "entrar", "entrar no computador", "entrar no pc", "acessar computador", "acessar pc", "computador", "primeiro acesso"],
        "text": f"""
📚 **Alunos e Professores Senac Camaquã**<br><br>
👤 Clique em **"Novo Usuário"** na tela inicial.<br><br>
📧 **E-mail:** SeuCPF@senacrs.edu.br  
*(Ex: 12345678910@senacrs.edu.br)*<br><br>
🔑 **Senha:** Sua Data de Nascimento no formato **DDMMAAAA + #Educ**  
*(Ex: 30032020#Educ)*<br><br>
⚠️ *Obs: A senha padrão só funciona se nunca foi alterada.*  
❓ Em caso de problemas ou esquecimento, procure o **Rodrigo na Secretaria**.
                    """,
        # "image_url": f"{BASE_IMAGE_URL}Tela+de+Login"
        "image_url": f"{BASE_IMAGE_URL}login/tela_login.jpg"
    },
    "login_visitante": {
        "keywords": ["visitante", "convidado", "acesso especial", "login visitante", "login convidado", "acesso visitante","acesso convidado", "login convidado", "entrar visitante", "entrar convidado", "acessar pc visitante", "acessar pc convidado"],
        "text": f"""
🧑‍💼 **Acesso Visitantes**<br><br>
🔑 **Login:** camaqua01@senacrs.edu.br<br>
🔐 **Senha:** Escola.Senac.01
                    """,
        # "image_url": f"{BASE_IMAGE_URL}Tela+de+Login"
        "image_url": f"{BASE_IMAGE_URL}login/tela_login.jpg"
    },
        "login_wifi": {
        "keywords": ["wifi", "senha wifi", "internet", "wifi internet"],
        "text": f"""                  
📶 **Rede Wi‑Fi Visitantes:** Senac Visitantes  
🔑 **Senha Wi‑Fi:** trijuntos<br><br>

📶 **Como conectar ao Wi‑Fi SENAC VISITANTES**<br><br>

1️⃣ **Ativar Wi‑Fi**  
➡️ Deslize a partir do topo da tela para baixo para abrir o painel de configurações rápidas.  
➡️ Toque no ícone de Wi‑Fi e mantenha pressionado.<br><br>

2️⃣ **Selecionar Rede**  
📡 No painel de Wi‑Fi, toque na rede **“SENAC VISITANTES”**.<br><br>

3️⃣ **Inserir Senha**  
🔑 Digite a senha **trijuntos** (sem aspas) e toque em **Conectar**.  
✅ Se a senha estiver correta, seu celular se conectará à rede.<br><br>

4️⃣ **Verificar Conexão**  
📲 Uma vez conectado, o ícone de Wi‑Fi mudará para indicar a conexão.  
🌐 Abra um navegador ou aplicativo que use internet para confirmar que deu certo.

                    """,
        "image_urls": [
        f"{BASE_IMAGE_URL}wifi/wifi.jpg",
        f"{BASE_IMAGE_URL}wifi/wifi2.jpg",
        f"{BASE_IMAGE_URL}wifi/wifi3.jpg"
    ]
 },
    "ativar_office": {
        "keywords": ["ativar office", "ativa office", "ativar ofice", "ativa ofice", "ativar word", "ativa word", "ativar excel", "ativa excel", "licença office"],
        "text": f"""
✅ **Ativar o Pacote Office**<br><br>
1️⃣ **Abrir o Office**<br>
📂 Abra qualquer aplicativo (Word, Excel). Vai aparecer a janela de login.<br><br>
2️⃣ **Entrar ou Criar Conta**<br>
👆 Clique em **“Entrar ou Criar uma conta”**.<br><br>
3️⃣ **Colocar Login e Senha**<br>
📧 Digite seu e‑mail **SeuCPF@senacrs.edu.br**<br>
🔑 Senha: a mesma do login do computador.<br><br>
4️⃣ **Trocar Senha (se pedir)**<br>
♻️ Insira a senha atual, depois a nova e confirme.<br><br>
5️⃣ **Aceitar Contrato**<br>
📜 Na tela de licença, clique em **“Aceitar”**.<br><br>
6️⃣ **Finalizar**<br>
🎉 Pronto, Office ativado!
                    """,
        "image_urls": [
        f"{BASE_IMAGE_URL}ativarPacoteOffice/ativar.png",
        f"{BASE_IMAGE_URL}ativarPacoteOffice/ativar1.png",
        f"{BASE_IMAGE_URL}ativarPacoteOffice/ativar2.png",
        f"{BASE_IMAGE_URL}ativarPacoteOffice/ativar3.png",
        f"{BASE_IMAGE_URL}ativarPacoteOffice/ativar4.png"
    ]
    },
    "portal_aluno_acesso": {
        "keywords": ["portal do aluno", "acessar portal", "portal", "login portal"],
        "text": f"""
💻 **Acessar o Portal do Aluno**<br><br>
1️⃣ **Entrar no site** <br>
🌐 Acesse: [Senac-RS](https://www.senacrs.com.br/)<br><br>
2️⃣ **Portal do Aluno**<br>
👤 Clique no ícone de usuário (menu superior à direita)<br>
➡️ Escolha **“Portal do Aluno”**<br><br>
3️⃣ **Login**<br>
📧 Digite seu **CPF ou Matrícula**<br>
4️⃣ **Senha**<br>
🔑 Use sua **Data de Nascimento (DDMMAAAA)** ou a senha atual<br><br>
⚠️ **Observação**<br>
🔄 Na primeira vez, o sistema pedirá para trocar a senha (use regras de senha forte).<br>
❓ Em caso de esquecimento, procure a **Hellen ou o Rodrigo na Secretaria**.
                    """,
        "image_urls": [
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço00.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço01.png"        
        ]
    },
    "solicitar_servico": {
        "keywords": ["solicitar serviço", "justificativa", "atestado escolar", "protocolo"],
        "text": f"""
📄 **Solicitar Serviço/Protocolo (Portal do Aluno)**<br><br>
1️⃣ **Entrar no Portal do Aluno**<br>
🌐 Acesse o Portal (veja o tópico *portal do aluno* se precisar).<br><br>
2️⃣ **Ambiente do Estudante**<br>
🎓 Clique em **“Ambiente do Estudante”**.<br><br>
3️⃣ **Autoatendimento**<br>
📋 No menu à esquerda, vá em **“Autoatendimento”**<br>
➡️ **“Solicitar Serviço”** (botão laranja).<br><br>
4️⃣ **Escolher Serviço**<br>
📝 Selecione o serviço desejado (ex.: **“Justificativa de Faltas”**).<br><br>
5️⃣ **Preencher Dados**<br>
🆔 Informe sua **Matrícula** (Selecione o curso atual)<br>
💬 Escreva suas **Observações**<br>
📎 **Anexe o arquivo** (atestado, etc.).<br><br>
6️⃣ **Enviar Solicitação**<br>
✅ Revise e clique em **Enviar** duas vezes para confirmar.
                    """,
        "image_urls": [
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço00.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço01.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço02.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço03.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço04.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço05.png",      
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço06.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço07.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço08.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço09.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço10.png",
        f"{BASE_IMAGE_URL}serviçosSecretaria/Serviço11.png"
        ]
    },
    "justificativa_falta": {
        "keywords": ["justificar falta", "atestado medico", "atraso justificativa"],
        "text": f"""
📅 **Justificativa de Faltas**<br><br>
📄 **Documentos**<br>
🩺 Devem ser amparados por documentos legais (atestado médico, convocação, etc.).<br><br>
⏰ **Prazo**<br>
📌 O atestado deve ser lançado no máximo **até 2 dias úteis** no Portal do Aluno.<br><br>
🛠️ **Como Lançar** <br>
➡️ Siga o passo a passo de **“Solicitar Serviço”** no Portal do Aluno.
                    """,
        "image_url": "" 
    },
    "trocar_senha_computador": {
        "keywords": ["trocar senha", "trocar", "senha", "alterar senha pc", "senha forte"],
        "text": f"""
🔑 **Troca de Senha do Computador/Rede**<br><br>
1️⃣ **Abrir Menu de Segurança**<br>
⌨️ Aperte as teclas **Ctrl + Alt + Delete**<br><br>
2️⃣ **Alterar Senha**<br>
🖱️ Clique em **“Alterar uma senha”**<br><br>
3️⃣ **Preencher Campos**<br>
🔒 Digite:<br>
- **Senha Atual**<br>
- **Nova Senha**<br>
- **Confirmar Nova Senha**<br><br>
💡 **Dicas de Senha Forte**<br>
✔️ Mínimo de **8 caracteres**<br>
🔠 Letras maiúsculas e minúsculas<br>
🔢 Números<br>
🔣 Caracteres especiais (ex.: !, @, #)
                    """,
        "image_urls": [
        f"{BASE_IMAGE_URL}trocaSenha/troca.jpg",
        f"{BASE_IMAGE_URL}trocaSenha/troca1.jpg",
        f"{BASE_IMAGE_URL}trocaSenha/troca2.png"        
        ]
    },
    "biblioteca_online": {
        "keywords": ["biblioteca online", "livros digitais", "pergamum"],
        "text": f"""
📚 **Acesso à Biblioteca Online (Minha Biblioteca)** <br><br>
1️⃣ **Entrar no site**<br>
🌐 Acesse o [Site do Senac-RS](https://www.senacrs.com.br/page/bibliotecas/) e vá em **“Bibliotecas”**<br><br>
2️⃣ **Localizar Minha Biblioteca**<br>
📖 Role a página até encontrar o logo **“Minha Biblioteca”**<br><br>
3️⃣ **Fazer Login** <br>
🔑 Insira seu **login e senha do Pergamum**<br>
❓ Se ainda não tiver, solicite na **Secretaria com o Rodrigo.**<br><br>
✨ **Vantagem**<br>
📚 O portal oferece acesso a mais de **11 mil livros digitais**
                    """,
        "image_urls": [
        f"{BASE_IMAGE_URL}biblioteca/biblioteca.png",
        f"{BASE_IMAGE_URL}biblioteca/biblioteca1.png",
        f"{BASE_IMAGE_URL}biblioteca/biblioteca2.png",
        f"{BASE_IMAGE_URL}biblioteca/biblioteca3.png",
        f"{BASE_IMAGE_URL}biblioteca/biblioteca4.png"   
        ]
    },
    "emprestimo_livros": {
        "keywords": ["emprestimo livro", "renovacao", "multa biblioteca"],
        "text": f"""
📖 **Empréstimo de Livros – Biblioteca Física** <br><br>
📚 **Empréstimo** <br>
👉 Escolha o livro na área de convivência e leve-o à **Secretaria** para registro. <br><br>
⏳ **Prazo** <br>
📌 7 dias corridos para devolução. <br><br>
🔄 **Renovação** <br>
🗓️ É possível renovar por +7 dias, mas o pedido deve ser feito **dentro do prazo inicial**. <br><br>
💰 **Multa** <br>
⚠️ R$ 1,00 por cada dia de atraso.
                    """,
        "image_url": ""
    },
    "cursos": {
        "keywords": ["cursos", "cursos livres", "cursos tecnicos", "ead", "graduação"],
        "text": f"""
🎓 **Conheça Nossas Áreas de Cursos!** <br><br>
📘 **FIC e Livres** <br>
➡️ [Portfólio de Cursos FICs Presenciais](https://www.senacrs.com.br/cursosLivres)<br><br>
📗 **Técnicos** <br>
➡️ [Portfólio de Cursos Técnicos Presenciais](https://www.senacrs.com.br/cursosTecnicos)<br><br>
💻 **EAD (FIC, Técnico, Pós)** <br>
➡️ [Portfólio de cursos FIC, Técnico e Pós EAD](https://www.ead.senac.br/niveis-de-ensino/)<br><br>
➡️**Cursos gratuitos (PSG)**<br>
➡️ [Vagas PSG](https://www.senacrs.com.br/hotsite/psg/partials/vagas-filter.php)<br><br>
⚠️ **Dica Importante** <br>
📍 Para visualizar vagas gratuitas, selecione Camaquã na página.
                    """,
        "image_url": f"{BASE_IMAGE_URL}imagens/Curso PSG.png"
    },
    "contatos_cursos": {
        "keywords": ["whatsapp", "consultoras", "contato cursos"],
        "text": f"""
📞 **Contatos das Consultoras de Cursos**<br><br>

👩‍💼 **Laurielle**<br>
➡️ [Clique para falar](https://api.whatsapp.com/send/?phone=5551999160202&text&type=phone_number&app_absent=0)<br><br>

👩‍💼 **Thais**<br>
➡️ [Clique para falar](https://api.whatsapp.com/send/?phone=5551985942119&text&type=phone_number&app_absent=0)<br><br>

👩‍💼 **Tailine**  <br>
➡️ [Clique para falar](https://api.whatsapp.com/send/?phone=5551991246334&text&type=phone_number&app_absent=0)<br><br>

                    """,
        "image_url": ""
    },
    "contato_secretaria": {
        "keywords": ["falar com secretaria", "contato secretaria"],
        "text": f"""
💬 **Contato da Secretaria (WhatsApp)**<br>

📲 [Clique para falar com a Secretaria](https://api.whatsapp.com/send/?phone=5551992680906&text&type=phone_number&app_absent=0)

                    """,
        "image_url": ""
    },
    "documentos_entrega": {
        "keywords": ["certificado", "diploma", "atestado de matricula", "prazo"],
        "text": f"""
📄 **Certificados, Diplomas e Atestados**<br><br>

🎓 **Certificado/Diploma**<br>
📅 Disponíveis em até **10 dias úteis** após o protocolo **e** o professor fechar todos os diários de turma.<br><br>

📑 **Atestado de Matrícula Padrão**<br>
🌐 Retire diretamente pelo **Portal do Aluno**<br>
➡️ Ambiente do Estudante > Página Principal > Atestado de Matrícula<br><br>

📝 **Atestado Customizado**<br>
📋 Abra um protocolo (veja *“Solicitar Serviço”*)<br>
✍️ Descreva o que precisa nas observações  <br>
⏰ Prazo: **6 dias úteis**

                    """,
        "image_url":""
    },
    "pagamentos": {
        "keywords": ["pagar curso", "boleto", "pix", "cartao", "financeiro", "pagar"],
        "text": f"""
💰 **Pagamento de Cursos**<br><br>

💻 **Portal do Aluno**<br>
➡️ No menu, selecione **Página Principal** > **Financeiro**<br>
💳 Escolha pagar por **Boleto**, **Pix** ou **Cartão de Crédito**<br><br>

🏫 **Presencial**<br>
👩‍💼 Procure pelo **Tainã** ou **Tatiane** no setor financeiro da escola<br><br>

📲 **WhatsApp Financeiro**  
➡️ [Clique aqui](https://api.whatsapp.com/send/?phone=5551991701052&text&type=phone_number&app_absent=0)

                    """,
        "image_url": ""
    },
    "boletim": {
        "keywords": ["boletim", "notas", "ver nota"],
        "text": f"""
📊 **Acesso ao Boletim**<br><br>

1️⃣ **Entrar no Portal do Aluno**<br>
🌐 Acesse o Portal (veja o tópico *“Portal do Aluno”* se precisar)<br><br>

2️⃣ **Abrir Boletim**<br>
📑 No menu à direita, clique em **“Boletim”**<br><br>

3️⃣ **Selecionar Curso**<br>
🎓 Escolha seu curso e as **notas aparecerão** na tela

                    """,
        "image_url": ""
    },
    "cursos_gratuitos": {
        "keywords": ["psg", "gratuitos", "vagas gratuitas", "inscrever cursos"],
        "text": f"""
🆓 **Cursos Gratuitos (PSG)**<br><br>

🌐 **Acesse o site**<br>
➡️ [Acesso às vagas](www.senacrs.com.br/hotsite/psg/partials/vagas-filter.php)<br><br>

🔎 **Buscar vagas**<br>
📍 Procure por oportunidades em **Camaquã**<br><br>

📋 **Requisitos**<br>
✅ Confira os requisitos de participação<br><br>

📝 **Inscrição**<br>
✍️ Inscreva-se para concorrer às vagas

                    """,
        "image_url": ""
    },
    "trabalhe_conosco": {
        "keywords": ["trabalhe conosco", "vagas emprego", "oportunidades trabalho"],
        "text": f"""
💼 **Trabalhe Conosco (Vagas Senac)**<br><br>

🌐 **Acesse o site**<br>
➡️ [Veja aqui](https://www.trabalhenosistema.com.br/)<br><br>

👤 **Cadastro**<br>
📝 Faça login e cadastre seus dados<br><br>

📢 **Acompanhe Vagas**<br>
🔎 Veja as oportunidades disponíveis no site<br>
📱 Confira também nas redes sociais do **Senac Camaquã**

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
def ask():
    user_query = request.json.get("query", "").lower()

    for key, value in FAQ_M365.items():
        if any(keyword in user_query for keyword in value["keywords"]):
            response = {"text": value["text"]}

            # Se houver várias imagens
            if "image_urls" in value:
                response["image_urls"] = value["image_urls"]
            # Se houver só uma
            elif "image_url" in value:
                response["image_url"] = value["image_url"]

            return jsonify(response)

    return jsonify({"text": "Desculpe, não encontrei nada sobre isso."})


if __name__ == '__main__':
    app.run(debug=True)

