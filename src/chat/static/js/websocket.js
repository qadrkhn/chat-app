// Here creating a WebSocket connection and sending a message to the server
document.addEventListener('DOMContentLoaded', () => {
    const websocketContainer = document.getElementById('the-message-to-send');
    const messageContainer = document.getElementById('messages-area');

    const websocketUrl = `ws://${window.location.host}/websocket/`;

    const websocket = new WebSocket(websocketUrl);

    // Log message from the consumer
    websocket.onmessage = (event) => {
        console.log('Consumer message:', event.data);
    };

    // Event listener for the button
    const sendMessagebutton = document.getElementById('send-message-button');
    sendMessagebutton.addEventListener('click', () => {
        // Send WebSocket message when the button is clicked
        const message = websocketContainer.value;
        if (message === '') { return; }

        // below lines get the user id that is receiving the message from the url
        let receiverId = null;
        const path = window.location.pathname;
        const lastSlashIndex = path.lastIndexOf('/');
        if (lastSlashIndex !== -1) {
            receiverId = path.charAt(lastSlashIndex - 1);
        }

        const messageToJSON = `{
            "type" : "new_message",
            "receiver" : "${receiverId}",
            "message" : "${message}"
        }`
        websocket.send(messageToJSON);
        websocketContainer.value = '';

        messageContainer.insertAdjacentHTML('beforeend',
            `<section class="to">
            <div class="details">
                <p>2024-01-30</p>
                <div class="status"><div></div><div></div></div>
                <p>10:55:02</p>
            </div>
            <div class="message">
                <p style="overflow-wrap: anywhere;">${message}</p>
            </div>
            </section>`
        );
        websocketContainer.value = '';

    });

});
