
from chat.models import Message, UserChannel
from accounts.models import Account

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

import json

"""
Scope used in consumers is a dictionary containing information about the connection, including the request, the user, and the path of the connection.
The scope is passed to the consumer when the connection is made.
Scope resembles the request object in synchronous views.
We can read session in consumer but cannnot store values in session in consumer.
"""

class ChatConsumer(WebsocketConsumer):
    # This method is called when the websocket is handshaking as part of the connection process
    def connect(self):
        # Accept the connection
        self.accept()

        # Save the channel name in the database
        try:
            user = self.scope['user']
            channel_name = self.channel_name
            user_channel = UserChannel.objects.create(user=user, channel_name=channel_name)
            # user_channel.save()

        except Exception as e:
            print(e)

    # This method is called when the websocket is receiving a message from the client
    def receive(self, text_data=None, bytes_data=None):
        # Convert text_data to a dictionary
        try:
            text_data_json = json.loads(text_data)
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)

        # save the message in the database
        try:
            sender = self.scope['user']
            receiver = text_data_json['receiver']
            content = text_data_json['message']
        except Exception as e:
            print(e)

        if all([sender, receiver, content]):
            try:
                receiver = Account.objects.get(id=receiver)
            except Account.DoesNotExist:
                print("Receiver does not exist")
                return
            message = Message.objects.create(sender=sender, receiver=receiver, content=content)
            message.save()

        try:
            data = {
                'type' : 'receive_function',
                'type_of_message' : 'new_message',
                'message' : content,
            }
            channel_name = UserChannel.objects.get(user=receiver).channel_name
            # Send the message to the layer
            async_to_sync(self.channel_layer.send)(
                channel_name, data
            )
        except Exception as e:
            print(e)

        return super().receive(text_data, bytes_data)

    # This method is called when the websocket is disconnected
    def disconnect(self, close_code):
        # Client sends 1001 code when the user moves to another page
        print("Disconnected with code: ", close_code)
        return super().disconnect(close_code)

    # Consumer must have a receiver method to receive data from the layer
    # This method will be called when the consumer receives a message from the layer
    # Name of this function matters. This is specified in the 'type' key of the data dictionary that is sent to the layer
    # This method is called when the consumer receives a message from the layer
    def receive_function(self, the_data_that_will_come_from_the_layer):
        print(the_data_that_will_come_from_the_layer)
        data = json.dumps(the_data_that_will_come_from_the_layer)
        self.send(text_data=data)
