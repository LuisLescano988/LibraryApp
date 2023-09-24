from django.urls import path, include
from .views import UserLoginView, UserSignUpView, UserTokenTestView

urlpatterns = [
    path('signup/',  UserSignUpView.as_view(), name='sign_up'),
    path('login/',  UserLoginView.as_view(), name='login'),
    path('test_token/',  UserTokenTestView.as_view(), name='test_token'),
]