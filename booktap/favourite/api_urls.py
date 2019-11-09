from django.urls import path
from favourite import views


urlpatterns = [
    path('getwishlist/', views.getwishlist, name='getwishlist'),
    path('postwishlist/', views.postwishlist, name='postwishlist'),

]