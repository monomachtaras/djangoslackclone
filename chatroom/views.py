from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ProfileForm


class MainPage(TemplateView):
    template_name = "chatroom/base.html"


class RegistrationView(FormView):
    template_name = "registration/registration_form.html"
    form_class = ProfileForm

    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


