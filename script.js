document.addEventListener('DOMContentLoaded', () => {
    // Variáveis do Chatbot
    const iconeChat = document.querySelector('.icone-assistente');
    const popupChat = document.querySelector('.popup-assistente');
    const botaoMinimizar = document.getElementById('minimizar-chat');
    const inputUsuario = document.getElementById('input-usuario');
    const botaoEnviar = document.getElementById('enviar-pergunta');
    const conversaContainer = document.getElementById('conversa-container');

    // Variáveis do Pop-up de Feedback
    const popupFeedback = document.getElementById('feedback-popup');
    const fecharPopupFeedback = document.getElementById('fechar-popup-feedback');
    const feedbackLink = popupFeedback.querySelector('.botao-feedback');

    // Substitua esta URL pela URL do seu servidor Render após a implantação
    //const SERVER_URL = 'http://localhost:5000/ask'; // Para testar localmente
    const SERVER_URL = 'https://chatbot-m365-ads.onrender.com/ask';

    // Lógica do Chatbot
    // Abrir chat ao clicar no ícone
    iconeChat.addEventListener('click', () => {
        popupChat.classList.add('aberto');
        iconeChat.style.display = 'none'; // Esconde o ícone
    });

    // Minimizar chat 
    if (botaoMinimizar) { 
        botaoMinimizar.addEventListener('click', () => { 
            popupChat.classList.remove('aberto'); 
            iconeChat.style.display = 'flex'; // Exibe o ícone novamente 
    });

}

    // Função para adicionar mensagens ao chat
    function adicionarMensagem(data, remetente) {
        const divMensagem = document.createElement('div');
        divMensagem.classList.add('mensagem');
        if (remetente === 'usuario') {
            divMensagem.classList.add('usuario-mensagem');
        } else {
            divMensagem.classList.add('bot-mensagem');
        }

        // Renderiza Markdown como HTML
        if (typeof marked !== 'undefined') {
            divMensagem.innerHTML = marked.parse(data.text);
        } else {
            divMensagem.textContent = data.text;
        }

        conversaContainer.appendChild(divMensagem);

        // Se houver várias imagens
        if (data.image_urls && Array.isArray(data.image_urls)) {
            data.image_urls.forEach(url => {
                const imgElement = document.createElement('img');
                imgElement.src = url;
                imgElement.classList.add('mensagem-imagem');
                conversaContainer.appendChild(imgElement);
            });
        } else if (data.image_url) {
            // Suporte para uma única imagem
            const imgElement = document.createElement('img');
            imgElement.src = data.image_url;
            imgElement.classList.add('mensagem-imagem');
            conversaContainer.appendChild(imgElement);
        }

        conversaContainer.scrollTop = conversaContainer.scrollHeight;
    }

    // Função para enviar pergunta ao backend
    async function enviarPergunta() {
        const pergunta = inputUsuario.value.trim();
        if (pergunta === '') {
            return;
        }

        adicionarMensagem({ text: pergunta }, 'usuario');
        inputUsuario.value = '';

        try {
            const response = await fetch(SERVER_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: pergunta }),
            });

            if (!response.ok) {
                throw new Error('Erro na comunicação com o servidor.');
            }

            const data = await response.json();

            setTimeout(() => {
                adicionarMensagem(data, 'bot');
            }, 500);

        } catch (error) {
            console.error("Erro ao enviar pergunta:", error);
            adicionarMensagem({ text: "Desculpe, não consigo me conectar. Tente novamente mais tarde." }, 'bot');
        }
    }

    botaoEnviar.addEventListener('click', enviarPergunta);
    inputUsuario.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            enviarPergunta();
        }
    });

    // Lógica do Pop-up de Feedback
    // Exibe após 30 segundos
    setTimeout(() => {
        popupFeedback.style.display = 'flex';
    }, 30000);

    // Fechar pop-up de feedback
    fecharPopupFeedback.addEventListener('click', () => {
        popupFeedback.style.display = 'none';
    });

    // Link do formulário de feedback
    feedbackLink.href = "https://forms.office.com/r/mpeD1i1LxM?origin=lprLink";
});