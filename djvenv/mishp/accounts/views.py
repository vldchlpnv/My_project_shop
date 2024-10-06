from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignInForm

class ViewForRegistration(generic.CreateView):
    form_class = SignInForm   # форма для заполнения для регистрации(лучше кастомизировать встроенная как то не очень)
    success_url = reverse_lazy("login")    # куда будет отправлен пользовательно после успешной регистрации
    template_name = 'registration/singin.html'    # имя шаблона регистрации

