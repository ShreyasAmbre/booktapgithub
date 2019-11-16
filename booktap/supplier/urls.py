from django.urls import path
from supplier import views
from supplier.views import Profile

urlpatterns = [
    # path('supplierprofile', views.supplierprofile, name='supplierprofile'),
    path('/<username>/', Profile.as_view()),
]
