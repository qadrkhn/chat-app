
from accounts.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('register/', Register.as_view(), name = 'register-view'),
    path('login/', Login.as_view(), name = 'login-view'),
    path('logout/', Logout.as_view(), name = 'logout-view')

]
