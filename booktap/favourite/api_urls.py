from django.urls import path
from favourite import views


urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
]