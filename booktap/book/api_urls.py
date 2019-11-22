from django.urls import path
from book import views
from book.views import EbookView
from book.views import Search
urlpatterns = [
    path('book/', views.book, name='book'),
    path('ebook/', views.ebook, name='book'),
    # path('ebooksearch/', views.ebooksearch, name='book'),
    path('getbookreviewrecords/', views.getbookreviewrecords, name='getbookreviewrecords'),
    path('postbookreviewrecords/', views.postbookreviewrecords, name='postbookreviewrecords'),
    path('novelsebook/', views.novelsebook, name='novelsebook'),
    path('adventureebook/', views.adventureebook, name='adventureebook'),
    path('autobiographyebook/', views.autobiographyebook, name='autobiographyebook'),
    path('EbookView/<int:id>/', EbookView.as_view()),
    path('Search/<int:id>/', Search.as_view()),
    # path('search/<int:id>/', views.search, name='search'),
]

