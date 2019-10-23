from django.urls import path

from pro import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    path('userlist', views.userlist, name='userlist'),
]
