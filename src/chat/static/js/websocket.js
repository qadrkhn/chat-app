// Here creating a WebSocket connection and sending a message to the server
document.addEventListener('DOMContentLoaded', () => {
    const websocketContainer = document.getElementById('the-message-to-send');
    const messageContainer = document.getElementById('messages-area');

    const websocketUrl = `ws://${window.location.host}/websocket/Qadeer/`;

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
        const messageToJSON = `{
            "type" : "new_message",
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
