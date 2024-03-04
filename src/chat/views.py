
from django.views import View
from django.shortcuts import render, redirect




class Main(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home-view')
        return render(request = request, template_name = 'chat/main.html')

class Home(View):
    def get(self, request):
        return render(request = request, template_name = 'chat/home.html')

class ChatPerson(View):
    def get(self, request):
        return render(request = request, template_name = 'chat/chat_person.html')
