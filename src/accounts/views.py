
from accounts.tasks import send_confirmation_email
from docker.workers.otp_worker.otp_tasks import send_email_otp, send_mobile_otp

from django.views import View
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

from celery import group

class Login(View):
    def get(self, request):
        return render(request = request, template_name = 'login.html')

    def post(self, request):
        context = {}
        user = None

        data = self.request.POST.dict()
        data.pop('csrfmiddlewaretoken')

        try:
            user = authenticate(request = request, **data)
        except Exception as e:
            context = {
                'errors': [str(e)]
            }

        if user is not None:
            login(request, user)
            otp_task_group = group(send_email_otp.s(), send_mobile_otp.s())
            otp_task_group.apply_async()
            return redirect('home-view')
        else:
            context = {
                'errors': ['Invalid credentials']
            }
            return render(request = request, template_name = 'login.html', context = context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login-view')

class Register(View):
    def get(self, request):
        return render(request = request, template_name = 'register.html', context = {})

    def post(self, request):
        context = {}
        user = None

        data = self.request.POST.dict()
        data.pop('csrfmiddlewaretoken')

        try:
            user = get_user_model().objects.create_user(**data)
        except Exception as e:
            context = {
                'errors': [str(e)]
            }

        authenticated_user = None
        if not context.get('errors', None):
            try:
                authenticated_user = authenticate(request = request, email = user.email, password = data['password'])
            except Exception as e:
                context = {
                    'errors': [str(e)]
                }

        if authenticated_user is not None:
            login(request, authenticated_user)
            send_confirmation_email.delay(user.email, "Lul")
            return redirect('home-view')
        else:
            return render(request = request, template_name = 'register.html', context = context)
