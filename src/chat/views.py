
from django.views import View
from django.shortcuts import render, HttpResponse




class Main(View):
    def get(self, request):
        return render(request = request, template_name = 'chat/main.html')

class Home(View):
    def get(self, request):
        return render(request = request, template_name = 'chat/home.html')

class ChatPerson(View):
    def get(self, request):
        return render(request = request, template_name = 'chat/chat_person.html')
