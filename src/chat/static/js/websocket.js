// Here creating a WebSocket connection and sending a message to the server
document.addEventListener('DOMContentLoaded', () => {
    const websocketContainer = document.getElementById('the-message-to-send');
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
        websocket.send(message);
        console.log('WebSocket message value:', message);
    });

});
