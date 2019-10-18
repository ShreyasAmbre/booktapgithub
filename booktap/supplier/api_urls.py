from django.urls import path
from supplier import views


urlpatterns = [
    path('suppliersdetails/', views.suppliersdetails, name='suppliersdetails'),
    path('suppliersrecords/', views.suppliersrecords, name='suppliersrecords'),

]