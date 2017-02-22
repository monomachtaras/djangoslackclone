
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormView
from .forms import UserCustomForm
from .models import CustomUser, Room
from  django.shortcuts import render



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


def chat_room(request, label='taras'):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chatroom/room.html", {
        'room': room,
        'messages': messages,
    })
