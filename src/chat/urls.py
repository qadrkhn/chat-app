
from chat.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', Main.as_view(), name = 'main-view'),
    path('home', Home.as_view(), name = 'home-view'),
    path('chat_person', ChatPerson.as_view(), name = 'chat-person'),
]
