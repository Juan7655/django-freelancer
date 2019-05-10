from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .forms import LoginForm


def logout_view(request):
    logout(request)
    return render(request, 'plain_message.html',
                  {'message': 'Logged out successfully',
                   'title': 'Logged out'})


class LoginPageView(TemplateView):
    template_name = "login.html"
    redirect_field_name = 'resume'

    def get(self, request: HttpRequest, *args, **kwargs):
        user_count = User.objects.all().count()

        if user_count == 0:
            user = User.objects.create_user(username='john', password='johnpassword')
            user.save()

        return render(request, 'login.html', {'login_form': LoginForm(),
                                              'title': 'Login'})

    def post(self, request: HttpRequest, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/resume')
            else:
                return render(request, 'plain_message.html',
                              {'message': 'User credentials are incorrect. Please, try again',
                               'title': 'Incorrect user'})

        form = LoginForm()
        return render(request, 'login.html', {'login_form': form})
