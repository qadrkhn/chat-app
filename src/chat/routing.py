
from chat.consumers import *

from django.urls import path


ASGI_urlpatterns = [
    path('websocket/', ChatConsumer.as_asgi(), name='websocket'),
]
