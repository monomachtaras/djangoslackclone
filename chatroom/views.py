from django.views.generic import TemplateView, ListView
from django.views import View
from .models import ChatUser


class MainPage(TemplateView):
    template_name = "chatroom/base.html"


class ListOfUser(ListView):
    model = ChatUser
    template_name = "base.html"


class UserLogin():
    pass


class UserRegister(View):

    def get(self, request):
        pass

    def post(self, request):
        pass

