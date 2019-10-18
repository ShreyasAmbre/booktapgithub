from django.urls import path
from book import views


urlpatterns = [
    path('book/', views.book, name='book'),
    path('ebook/', views.book, name='book'),
    path('bookreviewrecords/', views.bookreviewrecords, name='bookreviewrecords'),
]