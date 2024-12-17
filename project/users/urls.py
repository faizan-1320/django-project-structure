from django.urls import path
from . import views


urlpatterns = [
    path('users/register/',view=views.UserRegister.as_view(),name='register'),
    path('users/login/',view=views.UserLogin.as_view(),name='login'),
]