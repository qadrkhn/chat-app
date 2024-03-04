
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

"""
Scope used in consumers is a dictionary containing information about the connection, including the request, the user, and the path of the connection.
The scope is passed to the consumer when the connection is made.
Scope resembles the request object in synchronous views.
We can read session in consumer but cannnot store values in session in consumer.
"""

class ChatConsumer(WebsocketConsumer):
    # This method is called when the websocket is handshaking as part of the connection process
    def connect(self):
        self.accept()




    # This method is called when the websocket is receiving a message from the client
    def receive(self, text_data=None, bytes_data=None):
        print("Received message: ", text_data)
        return super().receive(text_data, bytes_data)

    # This method is called when the websocket is disconnected
    def disconnect(self, close_code):
        # Client sends 1001 code when the user moves to another page
        print("Disconnected with code: ", close_code)
        return super().disconnect(close_code)

    # Consumer must have a receiver method to receive data from the layer
    # This method will be called when the consumer receives a message from the layer
    def my_receiver(self, the_data_that_will_come_from_the_layer):
        print(the_data_that_will_come_from_the_layer)
