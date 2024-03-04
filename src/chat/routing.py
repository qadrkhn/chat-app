
from chat.consumers import *

from django.urls import path


ASGI_urlpatterns = [
    # as used in url_patterns <int:id>, we can also accpet arguments in the path of websocket
    # these arguments will be passed to the consumer and will be available in the scope inside 'url_route' key of the scope dictionary and inside 'kwargs' key of the 'url_route' dictionary
    path('websocket/<str:name>/', ChatConsumer.as_asgi(), name='websocket'),
]
