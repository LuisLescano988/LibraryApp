from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BookView, BookDetailView

urlpatterns = [
    path('all_books/', BookView.as_view(), name='all_books'),
    path('all_books/<int:pk>', BookDetailView.as_view(), name='detail_book'),
]