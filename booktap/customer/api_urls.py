from django.urls import path
from customer import views


urlpatterns = [
    path('customerorders/', views.customerorders, name='customerorders'),

    path('getcustomersearch/', views.getcustomersearch, name='getcustomersearch'),
    path('postcustomersearch/', views.postcustomersearch, name='postcustomersearch'),

    path('getcustomerreview/', views.getcustomerreview, name='getcustomerreview'),
    # path('postcustomerreview/', views.postcustomerreview, name='postcustomerreview'),
]