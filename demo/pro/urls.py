from django.urls import path

from pro import views

urlpatterns = [
    path('register', views.register, name='register'),
]
