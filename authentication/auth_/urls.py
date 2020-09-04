from django.urls import path
from django.http import HttpResponse

from . import views


urlpatterns = [
    path('', views.home, name="index"),
    path('signup/', views.registrationPage, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
