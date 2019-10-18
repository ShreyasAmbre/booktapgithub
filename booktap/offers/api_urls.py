from django.urls import path
from offers import views


urlpatterns = [
    path('discount/', views.discount, name='discount'),
]