from django.urls import path
from bookvideo import views

urlpatterns = [
    path('', views.bookvideo, name='bookvideo')
]