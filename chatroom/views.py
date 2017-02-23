from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, render
from .forms import UserCustomForm
from .models import CustomUser
from django.shortcuts import render



class MainPage(TemplateView):
    template_name = "chatroom/base.html"


class ListOfUsers(ListView):
    model = CustomUser
    template_name = "chatroom/list_of_users.html"


class RegistrationView(FormView):
    template_name = "registration/registration_form.html"
    form_class = UserCustomForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


class UserUpdate(UpdateView):
    model = CustomUser
    template_name = "chatroom/user_update.html"


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = 'chatroom/user_page.html'




def activation(request, key):
    profile = get_object_or_404(CustomUser, activation_key=key)
    if not profile.is_active:
        profile.is_active = True
        profile.activation_key = ''
        profile.save()
        return render(request, 'chatroom/base.html', {'message': "Your account was activated"})
    else:
        return render(request, 'chatroom/base.html', {'message': "Error! your account have already been activated"})
