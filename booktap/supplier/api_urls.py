from django.urls import path
from supplier import views
# from supplier.views import Profile

urlpatterns = [
    path('suppliersdetails/', views.suppliersdetails, name='suppliersdetails'),
    path('suppliersrecords/', views.suppliersrecords, name='suppliersrecords'),
    # path('/<username>/', Profile.as_view()),
]