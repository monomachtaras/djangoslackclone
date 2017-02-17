from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.MainPage.as_view()),
]
