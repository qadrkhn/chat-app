const url = `ws:${window.location.host}/websocket/`;
const websocket = new WebSocket(url);
// websocket.send('{"type" : "message" , "message" : "Hello"}')

websocket.onmessage = (event) => {
    console.log(event);
}
console.log(websocket);
