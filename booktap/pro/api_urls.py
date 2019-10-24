from django.urls import path

from pro import views
from pro.views import *

urlpatterns = [
    path('users/', views.users, name='pro'),
    path('loginapi/', views.loginapi, name='loginapi'),
    # path('userlist/', views.userlist, name='pro'),


]