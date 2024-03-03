
from channels.generic.websocket import WebsocketConsumer

"""
Scope used in consumers is a dictionary containing information about the connection, including the request, the user, and the path of the connection.
The scope is passed to the consumer when the connection is made.
Scope resembles the request object in synchronous views.
"""

class ChatConsumer(WebsocketConsumer):
    # This method is called when the websocket is handshaking as part of the connection process
    def connect(self):
        self.accept()
        self.send(text_data='{ "type" : "message" , "code" : 200 , "message" : "Connection successful" }') # Message to send to client side confirming connection
        value = self.scope


    # This method is called when the websocket is receiving a message from the client
    def receive(self, text_data=None, bytes_data=None):
        print("Received message: ", text_data)
        self.send(text_data='{ "type" : "message" , "code" : 200 , "message" : "Message received" }')
        return super().receive(text_data, bytes_data)

    # This method is called when the websocket is disconnected
    def disconnect(self, close_code):
        # Client sends 1001 code when the user moves to another page
        print("Disconnected with code: ", close_code)
        return super().disconnect(close_code)
