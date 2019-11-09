from django.urls import path
from book import views

urlpatterns = [
    path('book/', views.book, name='book'),
    path('ebook/', views.book, name='book'),
    path('getbookreviewrecords/', views.getbookreviewrecords, name='getbookreviewrecords'),
    path('postbookreviewrecords/', views.postbookreviewrecords, name='postbookreviewrecords'),
]