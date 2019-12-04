from django.urls import path
from ElectronicBook import views
from ElectronicBook.views import EbookView

# from book.views import Search
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
    path('searchfn/<str:name>/', views.searchfn, name='searchfn'),
    # path('search/<int:id>/', views.search, name='search'),
    path('ratedfn/<int:id>', views.ratedfn, name='ratedfn'),
]

