from django.urls import path, include, re_path
from .views import UserLoginView, UserSignUpView
from . import views

urlpatterns = [
    path('signup/',  UserSignUpView.as_view(), name='sign_up'),
    path('login/',  UserLoginView.as_view(), name='login'),
    re_path('test_token', views.test_token),
]