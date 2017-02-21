from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'chatroom'
urlpatterns = [

    url(r'^$', views.MainPage.as_view(), name="main_page"),
    url(r'^registration$', views.RegistrationView.as_view(), name="registration"),
    url(r'^profile/(?P<pk>\d+)/', views.CustomUserDetailView.as_view(), name="user_detail"),

]
