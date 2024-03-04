
from chat.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home', Home.as_view(), name = 'home-view'),
    path('chat_person', ChatPerson.as_view(), name = 'chat-person'),
]
