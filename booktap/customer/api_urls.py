from django.urls import path
from customer import views


urlpatterns = [
    path('customerorders/', views.customerorders, name='customerorders'),
    path('customersearch/', views.customersearch, name='customersearch'),
    path('customerreview/', views.customerreview, name='customerreview'),

]