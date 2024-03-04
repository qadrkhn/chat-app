
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model



class Main(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home-view')
        return render(request = request, template_name = 'chat/main.html')

class Home(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('main-view')

        context = {}
        all_users = get_user_model().objects.all()
        context['all_users'] = all_users
        context['current_user'] = request.user
        return render(request = request, template_name = 'chat/home.html', context = context)

class ChatPerson(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['current_user'] = request.user
        user_id = kwargs.get('id')
        if user_id:
            user = get_user_model().objects.filter(id = user_id).first()
            if user:
                context['user_to_contact'] = user
        return render(request = request, template_name = 'chat/chat_person.html', context = context)
