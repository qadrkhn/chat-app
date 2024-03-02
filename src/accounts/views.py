
from django.views import View
from django.shortcuts import render, HttpResponse

class Login(View):
    def get(self, request):
        return render(request = request, template_name = 'login.html')

class Logout(View):
    def get(self, request):
        return HttpResponse('<h1>No logout for now, TODO later</h1>')

class Register(View):
    def get(self, request):
        return render(request = request, template_name = 'register.html')
