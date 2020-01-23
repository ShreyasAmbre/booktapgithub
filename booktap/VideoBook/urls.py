from django.urls import path
from VideoBook import views

urlpatterns = [
    path('', views.videobooks, name='videobooks'),
]