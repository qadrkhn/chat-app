
from chat.consumers import *

from django.urls import path


ASGI_urlpatterns = [
    path('websocket', anything.as_asgi(), name='websocket'),
]
