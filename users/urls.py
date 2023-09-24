from django.urls import path, include
from .views import UserLoginView, UserSignUpView, UserTokenTestView

urlpatterns = [
    path('signup/',  UserSignUpView.as_view(), name='sign_up'),
    path('login/',  UserSignUpView.as_view(), name='sign_up'),
    path('test_token/',  UserSignUpView.as_view(), name='sign_up'),
]