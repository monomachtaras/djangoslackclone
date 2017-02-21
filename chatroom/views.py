from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class MainPage(TemplateView):
    template_name = "chatroom/base.html"

