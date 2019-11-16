from django.urls import path
from customer import views
from customer.views import SingleEBookCustomerReviewView

urlpatterns = [
    path('customerorders/', views.customerorders, name='customerorders'),

    path('getcustomersearch/', views.getcustomersearch, name='getcustomersearch'),
    path('postcustomersearch/', views.postcustomersearch, name='postcustomersearch'),

    path('getcustomerreview/', views.getcustomerreview, name='getcustomerreview'),
    # path('postcustomerreview/', views.postcustomerreview, name='postcustomerreview'),
    path('SingleEBookCustomerReviewView/<int:id>/', SingleEBookCustomerReviewView.as_view()),
]