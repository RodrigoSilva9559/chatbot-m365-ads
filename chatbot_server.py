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
       "keywords": ["acesar","acesar computador","acesar compudador","acesso computador","acesso compudador", "login","loguin","logim","logn","loggin","loguin","loguin","loguin","loguin","loguin", "entrar","entar","entra","entrarr","entrarr","entrra","entarr","entar","entar","entar", "entrar no computador","entar no computador","entrar no compudador","entrar no compudador","entrar no compudador","entrar no compudador","entrar no compudador","entrar no compudador","entrar no compudador","entrar no compudador", "entrar no pc","entar no pc","entrar no pcc","entrar no pcc","entrar no pcc","entrar no pcc","entrar no pcc","entrar no pcc","entrar no pcc","entrar no pcc", "acessar computador","acesar computador","acessar compudador","acessar compudador","acessar compudador","acessar compudador","acessar compudador","acessar compudador","acessar compudador","acessar compudador", "acessar pc","acesar pc","acessar pcc","acessar pcc","acessar pcc","acessar pcc","acessar pcc","acessar pcc","acessar pcc","acessar pcc", "computador","compudador","computadorr","computado","computador","computador","computador","computador","computador","computador", "primeiro acesso","primeiro aceso","primeiro acsso","primeiro acseso","primeiro acsso","primeiro acsso","primeiro acsso","primeiro acsso","primeiro acsso","primeiro acsso", "iniciar","inicar","inicir","inicar","inicir","inicar","inicir","inicar","inicir","inicar", "começar","comecar","comessar","comecar","comessar","comecar","comessar","comecar","comessar","comecar", "abrir" ],
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
        "keywords": [ "visitante","visitanete","visistante","vizitante","vistante","visistnte","visittante","vissitante","visitant","visitnte", "convidado","convidaddo","convidad","convidaro","convidato","convidaod","conviddao","conviddado","convidadp","convidad0", "acesso especial","aceso especial","acesso espceial","acesso especia","aceso espcl","acso especial","acesso espcl","acesso espcia","acesso espceal","acesso espcll", "login visitante","logim visitante","loguin visitante","login visitant","login vizitante","login visistante","login vistante","login visitnte","login visitanete","login visistnte", "login convidado","logim convidado","loguin convidado","login convidaod","login convidato","login convida","login convdado","login convidaado","login convvidado","login convidaod", "acesso visitante","aceso visitante","acesso vizitante","acesso visitant","aceso visistante","acesso vistante","acesso visitnte","acesso visistnte","acesso visitanete","acesso visistnte", "acesso convidado","aceso convidado","acesso convidaod","acesso convidato","aceso convida","acesso convdado","acesso convidaado","acesso convvidado","acesso convidaod","acesso conviddao", "entrar visitante","entar visitante","entrar vizitante","entrar visitant","entrar visistante","entrar vistante","entrar visitnte","entrar visistnte","entrar visitanete","entrar visistnte", "entrar convidado","entar convidado","entrar convidaod","entrar convidato","entrar convida","entrar convdado","entrar convidaado","entrar convvidado","entrar convidaod","entrar conviddao" ],
        "text": f"""
🧑‍💼 **Acesso Visitantes**<br><br>
🔑 **Login:** camaqua01@senacrs.edu.br<br>
🔐 **Senha:** Escola.Senac.01
                    """,
        # "image_url": f"{BASE_IMAGE_URL}Tela+de+Login"
        "image_url": f"{BASE_IMAGE_URL}login/tela_login.jpg"
    },
        "login_wifi": {
        "keywords": [ "wifi","wfi","wi-fi","wi fi","wiffi","wifii","wify","wif","wifii","wifii", "senha wifi","senhaa wifi","senah wifi","senhaa wfi","senhaa wi-fi","senhaa wiffi","senhaa wify","senhaa wif","senhaa wifii","senhaa wifii", "internet","internt","internete","interne","intenet","inernet","internett","internete","internat","internat", "wifi internet","wfi internet","wi-fi internet","wi fi internet","wiffi internet","wifii internet","wify internet","wif internet","wifii internete","wifii internat", "rede wifi","rede wfi","rede wi-fi","rede wiffi","rede wify","rede wifii","rede wif","rede wifii","rede wifii","rede wify" ],
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
       "keywords": [ "ativar office","ativa office","ativar ofice","ativa ofice","ativar offfice","ativar offce","ativar offcie","ativar offise","ativar offece","ativar offise", "ativa ofice","ativa offce","ativa offcie","ativa offise","ativa offece","ativa offise","ativa offcie","ativa offce","ativa offise","ativa offece", "ativar ofc","ativa ofc","ativar off","ativa off","ativar offi","ativa offi","ativar offiice","ativa offiice","ativar offecee","ativa offecee", "ativar word","ativa word","ativar wrod","ativar wrd","ativar wor","ativar wod","ativar wordd","ativar worrd","ativar worde","ativar worl", "ativa word","ativa wrod","ativa wrd","ativa wor","ativa wod","ativa wordd","ativa worrd","ativa worde","ativa worl","ativa worde", "ativar wrld","ativa wrld","ativar wrldd","ativa wrldd","ativar worrld","ativa worrld","ativar wordee","ativa wordee","ativar worddd","ativa worddd", "ativar excel","ativa excel","ativar exel","ativar exl","ativar exccl","ativar excell","ativar excal","ativar exelc","ativar exel","ativar excsel", "ativa excel","ativa exel","ativa exl","ativa exccl","ativa excell","ativa excal","ativa exelc","ativa exel","ativa excsel","ativa excal", "ativar exell","ativa exell","ativar exelc","ativa exelc","ativar excele","ativa excele","ativar excele","ativa excele","ativar excele","ativa excele", "licença office","licenca office","licença ofice","licenca ofice","licença offce","licença offcie","licença offise","licença offece","licença offise","licença offcie", "licenca ofc","licença ofc","licenca off","licença off","licenca offi","licença offi","licenca offiice","licença offiice","licenca offecee","licença offecee", "word","wrod","worrd","wordd","worde","worl","wrld","wrd","woed","wrd", "excel","exel","exl","exell","excell","excal","exccl","exelc","excsel","excele", "power point","powerpoint","pwr point","pwrpoint","pwer point","pwerpoint","poer point","poerpoint","powr point","powrpoint", "powerpint","powerpintt","powerpint","powerpintt","powerpoit","powerpoitt","powerpoit","powerpoitt","powerpoin","powerpoin", "ativar powerpoint","ativa powerpoint","ativar pwr point","ativa pwr point","ativar poer point","ativa poer point","ativar powr point","ativa powr point","ativar powerpint","ativa powerpint", "ativar powerpoit","ativa powerpoit","ativar powerpoin","ativa powerpoin","ativar powerpoitt","ativa powerpoitt","ativar powerpoinn","ativa powerpoinn","ativar powerpoinnt","ativa powerpoinnt" ],
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
        "keywords": [ "portal do aluno","portal do alno","portal do alun","portal do alumo","portal do alino","portal do alumo","portal do aln","portal do alnoo","portal do alnu","portal do alino", "acessar portal","acesar portal","acessar portl","acessar portaal","acessar portel","acessar portao","acessar portla","acessar portaal","acessar portaal","acessar portaal", "portal","portl","portaal","portel","portao","prtal","poratl","portla","portaal","portaal", "login portal","logim portal","loguin portal","logn portal","login portl","login portaal","login portel","login portao","login portla","login poratl" ],
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
        "keywords": [ "solicitar serviço","solicitar servico","solicitar serviso","solicitar servisso","solicitar servicoo", "solicitar servico","solicitar servico","solicitar servico","solicitar servico","solicitar servico", "solicitar servico","solicitar servico","solicitar servico","solicitar servico","solicitar servico", "solicitar servico","solicitar servico","solicitar servico","solicitar servico","solicitar servico", "solicitar certificado","solicitar certficado","solicitar certifcado","solicitar certifcado","solicitar certifcadoo", "solicitar certifcado","solicitar certifcado","solicitar certifcado","solicitar certifcado","solicitar certifcado", "solicitar certifcado","solicitar certifcado","solicitar certifcado","solicitar certifcado","solicitar certifcado", "solicitar certifcado","solicitar certifcado","solicitar certifcado","solicitar certifcado","solicitar certifcado", "atestado escolar","atetsado escolar","atestdo escolar","atestado esolar","atestado escoolar", "atestado escolar","atestado escolar","atestado escolar","atestado escolar","atestado escolar", "atestado escolar","atestado escolar","atestado escolar","atestado escolar","atestado escolar", "atestado escolar","atestado escolar","atestado escolar","atestado escolar","atestado escolar", "protocolo","protcolo","protoclo","protocoolo","protocoll", "protocolo","protocolo","protocolo","protocolo","protocolo", "protocolo","protocolo","protocolo","protocolo","protocolo", "protocolo","protocolo","protocolo","protocolo","protocolo" ],
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
        "keywords": [ "justificar falta","justifcar falta","justficar falta","justifcar falt","justificar falata", "justificar falat","justificar falat","justifcar falat","justficar falata","justifcar falata", "justificar fta","justificar fatla","justificar flata","justifcar flta","justficar flata", "justificar falt","justifcar falt","justficar falt","justifcar falt","justficar falt", "atestado medico","atetsado medico","atestdo medico","atestado medco","atestado mediko", "atestado mediko","atestado mediko","atestado mediko","atestado mediko","atestado mediko", "atestado medik","atestado medik","atestado medik","atestado medik","atestado medik", "atestado med","atestado med","atestado med","atestado med","atestado med", "atraso justificativa","atraso justifcativa","atraso justifictiva","atraso justificava","atraso justificatiiva", "atraso justificativaa","atraso justifcava","atraso justifictva","atraso justificatva","atraso justificatvia", "atraso justifcativ","atraso justificativ","atraso justificativ","atraso justificativ","atraso justificativ", "atraso justificativ","atraso justificativ","atraso justificativ","atraso justificativ","atraso justificativ" ],
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
        "keywords": [ "trocar senha","trocar senhaa","trocar senah","trocar senh","trocar sennha","trocar sennhaa","trocar senhaa","trocar senahh","trocar sennh","trocar senahh", "trocar","troacr","trcar","trocarr","troka","tocar","troccar","trocarrr","trocarr","trocarrr", "senha","senhaa","senah","senh","sennha","sennhaa","senhaa","senahh","sennh","senahh", "alterar senha pc","alterar senhaa pc","alterar senah pc","alterar senh pc","alterar sennha pc","alterar sennhaa pc","alterar senhaa pc","alterar senahh pc","alterar sennh pc","alterar senahh pc", "senha forte","senhaa forte","senah forte","senh forte","sennha forte","sennhaa forte","senhaa forte","senahh forte","sennh forte","senahh forte" ],
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
        "keywords": [ "biblioteca online","bibliotca online","biblioteka online","bibliotca onlin","biblioteca onlin","biblioteca onlne","biblioteca olnine","biblioteca onlina","biblioteca onliine","biblioteca onlline", "biblioteca onlain","biblioteca onliene","biblioteca onlina","biblioteca onlien","biblioteca onlini", "livros digitais","livros digitas","livros digitai","livros digitall","livros digitails","livros digitasi","livros digtais","livros digtals","livros digtias","livros digtasi", "livros digitau","livros digitaz","livros digitais","livros digitass","livros digitaiis", "pergamum","pergamu","pergamun","pergammum","pergamumm","pergamunm","pergamummm","pergamummu","pergamummn","pergamummo", "pergamummi","pergamummu","pergamummo","pergamummn","pergamummm" ],
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
        "keywords": [ "emprestimo livro","emprestimo livr","emprestimo livor","emprestimo livru","emprestimo livvo", "emprestimo livvro","emprestimo livrro","empréstimo livro", "emprestimo livvro","emprestimo livvroo","emprestimo livvro", "emprstimo livro","emprstimo livr","emprstimo livor","emprstimo livru","emprstimo livvo", "emprestmo livro","emprestmo livr","emprestmo livor","emprestmo livru","emprestmo livvo", "renovacao","renovacão","renovaco","renovacau","renovacoo", "renovacãoo","renovacãoo","renovacãoo","renovacãoo","renovacãoo", "renovcao","renovcão","renovcau","renovcaoo","renovcãoo", "renovacã","renovacãa","renovacãao","renovacãu","renovacãoo", "multa biblioteca","multa bibliotca","multa biblioteka","multa bibliotce","multa bibliotecaa", "multa bibliotec","multa bibliotec","multa bibliotec","multa bibliotec","multa bibliotec", "multa bibliteca","multa biblitec","multa biblitekaa","multa biblitecaa","multa biblitec", "multa bibliteka","multa biblitekaa","multa biblitecaa","multa biblitec","multa biblitec" ],
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
        "keywords": [ "cursos","cursoss","cursso","curssos","cursu","curssu","curss","crusos","curssos","cursoss", "cursos livres","cursoss livres","cursso livres","curssos livres","cursu livres","curssu livres","curss livres","crusos livres","curssos livress","cursoss livress", "cursos tecnicos","cursoss tecnicos","cursso tecnicos","curssos tecnicos","cursu tecnicos","curssu tecnicos","curss tecnicos","crusos tecnicos","curssos tecnicos","cursoss tecnicos", "ead","eaad","eadd","eadd","eaad","eaddd","ead ","eads","eads","eadd", "graduação","graduacao","graduaçao","graduaçã","graduaçãao","graduaçãa","graduaçãu","graduaçãoo","graduaçã","graduaçãao" ],
        "text": f"""
🎓 **Conheça Nossas Áreas de Cursos!** <br><br>
📘 **FIC e Livres** <br>
➡️ [Portfólio de Cursos FICs Presenciais](https://www.senacrs.com.br/cursosLivres)<br><br>
📗 **Técnicos** <br>
➡️ [Portfólio de Cursos Técnicos Presenciais](https://www.senacrs.com.br/cursosTecnicos)<br><br>
💻 **EAD (FIC, Técnico, Pós)** <br>
➡️ [Portfólio de cursos FIC, Técnico e Pós EAD](https://www.ead.senac.br/niveis-de-ensino/)<br><br>

                    """,
        "image_url": ""        
    },
    "contatos_cursos": {
        "keywords": [ "whatsapp","watsapp","whatsap","whatspp","whatsappp","watssap","watsap","whatsap","whatsapppp","whatsappp", "consultoras","consultora","consultoras","consutoras","consultroras","consutlora","consultrra","consultroras","consultroras","consultroras", "vendas","venda","vndas","vndass","vendass","vendaz","vendazs","vendazss","vendazs","vendazss", "whats","wats","whatsz","whatz","whatsx","whatsc","whatsk","whatsq","whatsw","whatsv", "contato cursos","contato cursoss","contato cursso","contato curssos","contato cursu","contato curssu","contato curss","contato crusos","contato curssos","contato cursoss" ],
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
        "keywords": [ "falar com secretaria","falar com secretari","falar com secretaira","falar com secretária","falar com secrtaria", "falar com secetaria","falar com secretariia","falar com secretarria","falar com secretarai","falar com secretari", "falr com secretaria","falaar com secretaria","falar cm secretaria","falar com secetaria","falar com secretariia", "falar com secretari","falar com secretarai","falar com secretarria","falar com secretari","falar com secretari", "falar secretaria","falr secretaria","falaar secretaria","falar secetaria","falar secretari", "falar secretaira","falar secretária","falar secrtaria","falar secretariia","falar secretarria", "contato secretaria","contato secretari","contato secretaira","contato secretária","contato secrtaria", "contato secetaria","contato secretariia","contato secretarria","contato secretarai","contato secretari", "contato secretria","contato secretraria","contato secretari","contato secretari","contato secretari", "contato secetaria","contato secretariia","contato secretarria","contato secretarai","contato secretari", "cntato secretaria","contato secetaria","contato secretariia","contato secretarria","contato secretari" ],
        "text": f"""
💬 **Contato da Secretaria (WhatsApp)**<br>

📲 [Clique para falar com a Secretaria](https://api.whatsapp.com/send/?phone=5551992680906&text&type=phone_number&app_absent=0)

                    """,
        "image_url": ""
    },
    "documentos_entrega": {
       "keywords": [ "certificado","certifcado","certifcadoo","certifcado","certifcado","certifcado","certifcado","certifcado","certifcado","certifcado", "certifcado","certifcado","certifcado", "diploma","diplomaa","diplomma","diplomma","diplom","diplom","diplom","diplom","diplom","diplom", "diplom","diplom","diplom", "atestado de matricula","atetsado de matricula","atestdo de matricula","atestado d matricula","atestado de matrcula","atestado de matrciula","atestado de matriula","atestado de matrucula","atestado de matrcul","atestado de matrcul", "atestado de matrcula","atestado de matrcula","atestado de matrcula", "prazo","prazoz","praaz","prazzo","prazoo","praz","praz","praz","praz","praz", "praz","praz","praz" ],
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
        "keywords": [ "pagar curso","pagar curço","pagar curço","pagar cursso","pagar cursu","pagar curssu","pagar curss","pagar crusso","pagar curs","pagar curço", "boleto","boelto","bolto","boelto","boeltoo","boeltoo","boeltoo","boeltoo","boeltoo","boeltoo", "pix","piks","piz","pis","pixx","piix","pixi","pixz","pixs","pixc", "cartao","cartão","carto","cartan","cartaoo","cartao","cartã","cartãao","cartãu","cartãaoo", "financeiro","finaceiro","financero","finanseiro","financieiro","financieiroo","financieiro","financiero","financieiro","financieiro", "pagar","pagarr","pagr","paga","pagaar","pagarr","pagarr","pagarr","pagarr","pagarr","pagamento" ],
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
        "keywords": [ "boletim","boletin","boletimm","boletime","boletii","boletinm","boletm","boletmi","boletiin","boletiem", "boletimee","boletimm","boletimmm","boletinmm","boletiemm","boletime","boletimee","boletimm","boletiin","boletiem", "notas","nota","notaz","notass","notaas","notazs","notazss","nottas","nottaz","nottass", "nottazs","nottazss","notazzz","notazss","notazs","notasss","notaz","notazs","notazss","notazzz", "ver nota","ver notaa","ver notaz","ver notazs","ver notazss","ver notass","ver notaas","ver notazzz","ver notazs","ver notazss", "ver notazzz","ver notaz","ver notazs","ver notazss","ver notasss","ver notaz","ver notazs","ver notazss","ver notazzz","ver notaz" ],
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
        "keywords": [ "psg","psgg","psjg","pshg","psq","psqq","psjg","pshg","psggg","psgg","psjg","pshg", "gratuitos","gratuito","gratuitosss","gratuitosz","gratuitosx","gratuitosv","gratuitosw","gratuitosq","gratuitosk","gratuitosd","gratuitosf","gratuitosg", "vagas gratuitas","vagas gratuito","vagas gratutos","vagas gratitua","vagas gratituaas","vagas gratituz","vagas gratituss","vagas gratitux","vagas gratituw","vagas gratituk","vagas gratituf","vagas gratitug", "inscrever cursos","inscreve cursos","inscrevr cursos","inscreveer cursos","inscreve cursos","inscrev cursos","inscrevrr cursos","inscrevve cursos","inscrevver cursos","inscrevvr cursos","inscrevrs cursos","inscrevrss cursos","inscrevrz cursos" ],
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
       "keywords": [ "trabalhe conosco","trabalhe conoso","trabalhe conssco","trabalhe conoscco","trabalhe conosoo","trabalhe conossco","trabalhe conosskoo","trabalhe conosscoo","trabalhe conosskoo","trabalhe conosskoo", "trabalhe conoso","trabalhe conssco","trabalhe conoscco","trabalhe conosoo","trabalhe conossco","trabalhe conosskoo","trabalhe conosscoo","trabalhe conosskoo","trabalhe conosskoo","trabalhe conosskoo", "vagas emprego","vagas emprgo","vagas emrego","vagas empprego","vagas empprego","vagas emppregoo","vagas emppregu","vagas emppreguu","vagas emppregoo","vagas emppregoo", "vagas emprgo","vagas emrego","vagas empprego","vagas empprego","vagas emppregoo","vagas emppregu","vagas emppreguu","vagas emppregoo","vagas emppregoo","vagas emppregoo", "oportunidades trabalho","oportunidade trabalho","oportunidaes trabalho","oportunidaeds trabalho","oportunidaes trabalo","oportunidaes trablho","oportunidaes trbalho","oportunidaes trbalh","oportunidaes trbalhoo","oportunidaes trbalhoo", "oportunidade trabalho","oportunidaes trabalho","oportunidaeds trabalho","oportunidaes trabalo","oportunidaes trablho","oportunidaes trbalho","oportunidaes trbalh","oportunidaes trbalhoo","oportunidaes trbalhoo","oportunidaes trbalhoo" ],
        "text": f"""
💼 **Trabalhe Conosco (Vagas Senac)**<br><br>

🌐 **Acesse o site**<br>
➡️ [www.trabalhenosistema.com.br](www.trabalhenosistema.com.br)<br><br>

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
