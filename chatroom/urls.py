from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'chatroom'
urlpatterns = [
    url(r'^$', views.MainPage.as_view(), name="main_page"),

    # url(r'^list_of_users$', login_required(views.ListOfUser.as_view, name="register")),
]
