from django.urls import path

from pro import views
from pro.views import *

urlpatterns = [
    path('users/', views.users, name='pro'),
    # path('userlist/', views.userlist, name='pro'),


]