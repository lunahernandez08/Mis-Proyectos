const chatContainer = document.getElementById('chat-container');
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');

const API_KEY = 'AIzaSyAPViHYqzHYf6RylzmFBSdshnF2EoqhaOc';

async function sendMessage(message) {
    const response = await fetch('https://api.gemini.google.com/v1/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();
    console.log(data); // Imprime la respuesta completa en la consola
    return data.message;
}

sendButton.addEventListener('click', async () => {
    const userMessage = messageInput.value;
    messageInput.value = '';

    // Mostrar mensaje del usuario
    const userMessageElement = document.createElement('div');
    userMessageElement.classList.add('user-message');
    userMessageElement.textContent = userMessage;
    chatContainer.appendChild(userMessageElement);

    // Enviar mensaje a Gemini y mostrar la respuesta
    const botMessage = await sendMessage(userMessage);
    const botMessageElement = document.createElement('div');
    botMessageElement.classList.add('bot-message');
    botMessageElement.textContent = botMessage;
    chatContainer.appendChild(botMessageElement);

    // Desplazar el chat hacia abajo
    chatContainer.scrollTop = chatContainer.scrollHeight;
});
async function sendMessage(message) {
    try {
        const response = await fetch('https://api.gemini.google.com/v1/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`
            },
            body: JSON.stringify({ message })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        console.log(data); // Imprime la respuesta completa en la consola
        return data.message;

    } catch (error) {
        console.error('Error al enviar el mensaje:', error);
        return 'Hubo un problema al conectarse al servidor.';
    }
}
