
from chat.models import Message

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.db.models import Q


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
        context['all_users'] = all_users.exclude(id = request.user.id)
        context['current_user'] = request.user
        return render(request = request, template_name = 'chat/home.html', context = context)

class ChatPerson(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('main-view')
        context = {}
        messages = Message.objects.filter( Q(sender = request.user, receiver = kwargs.get('id')) | Q(sender = kwargs.get('id'), receiver = request.user)).order_by('created_at')
        context['current_user'] = request.user
        context['messages'] = messages
        user_id = kwargs.get('id')
        if user_id:
            user = get_user_model().objects.filter(id = user_id).first()
            if user:
                context['user_to_contact'] = user
        return render(request = request, template_name = 'chat/chat_person.html', context = context)
