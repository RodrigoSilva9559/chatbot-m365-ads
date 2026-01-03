document.addEventListener('DOMContentLoaded', () => {
    const iconeChat = document.querySelector('.icone-assistente');
    const popupChat = document.querySelector('.popup-assistente');
    const botaoMinimizar = document.getElementById('minimizar-chat');
    const inputUsuario = document.getElementById('input-usuario');
    const botaoEnviar = document.getElementById('enviar-pergunta');
    const conversaContainer = document.getElementById('conversa-container');

    const popupFeedback = document.getElementById('feedback-popup');
    const fecharPopupFeedback = document.getElementById('fechar-popup-feedback');
    const feedbackLink = popupFeedback.querySelector('.botao-feedback');

    //const SERVER_URL = 'http://localhost:5000/ask'; // teste na minha maquina
    const SERVER_URL = 'https://chatbot-m365-ads.onrender.com/ask';

    iconeChat.addEventListener('click', () => {
        popupChat.classList.add('aberto');
        iconeChat.style.display = 'none';
    });

    if (botaoMinimizar) { 
        botaoMinimizar.addEventListener('click', () => { 
            popupChat.classList.remove('aberto'); 
            iconeChat.style.display = 'flex';
    });

}

    function adicionarMensagem(data, remetente) {
        const divMensagem = document.createElement('div');
        divMensagem.classList.add('mensagem');
        if (remetente === 'usuario') {
            divMensagem.classList.add('usuario-mensagem');
        } else {
            divMensagem.classList.add('bot-mensagem');
        }

        if (typeof marked !== 'undefined') {
            divMensagem.innerHTML = marked.parse(data.text);
        } else {
            divMensagem.textContent = data.text;
        }

        conversaContainer.appendChild(divMensagem);

        if (data.image_urls && Array.isArray(data.image_urls)) {
            data.image_urls.forEach(url => {
                const imgElement = document.createElement('img');
                imgElement.src = url;
                imgElement.classList.add('mensagem-imagem');
                conversaContainer.appendChild(imgElement);
            });
        } else if (data.image_url) {
            const imgElement = document.createElement('img');
            imgElement.src = data.image_url;
            imgElement.classList.add('mensagem-imagem');
            conversaContainer.appendChild(imgElement);
        }

        conversaContainer.scrollTop = conversaContainer.scrollHeight;
    }

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


    setTimeout(() => {
        popupFeedback.style.display = 'flex';
    }, 30000);

    fecharPopupFeedback.addEventListener('click', () => {
        popupFeedback.style.display = 'none';
    });

    feedbackLink.href = "https://forms.office.com/r/mpeD1i1LxM?origin=lprLink";
});