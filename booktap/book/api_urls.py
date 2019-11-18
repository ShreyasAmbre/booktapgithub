from django.urls import path
from book import views
from book.views import EbookView

urlpatterns = [
    path('book/', views.book, name='book'),
    path('ebook/', views.book, name='book'),
    path('getbookreviewrecords/', views.getbookreviewrecords, name='getbookreviewrecords'),
    path('postbookreviewrecords/', views.postbookreviewrecords, name='postbookreviewrecords'),
    path('novelsebook/', views.novelsebook, name='novelsebook'),
    path('adventureebook/', views.adventureebook, name='adventureebook'),
    path('autobiographyebook/', views.autobiographyebook, name='autobiographyebook'),
    path('EbookView/<int:id>/', EbookView.as_view()),

]

