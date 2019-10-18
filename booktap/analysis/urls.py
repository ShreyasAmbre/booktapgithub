from django.urls import path
from analysis import views

urlpatterns = [
    # path('customercount/', views.customercount, name='customercount'),
    path('dashboard/', views.count, name='bookcount'),
]