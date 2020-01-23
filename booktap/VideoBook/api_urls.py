from django.conf.urls import url
from django.urls import path
from VideoBook import views
from VideoBook.views import VideoBookView, SearchList

urlpatterns = [
    path('getvideobooks/', views.getvideobooks, name='getvideobooks'),
    path('getvideobookreviewrecords/', views.getvideobookreviewrecords, name='getvideobookreviewrecords'),
    path('VideoBookView/<int:id>/', VideoBookView.as_view()),
    path('ratedfn/<int:id>', views.ratedfn, name='ratedfn'),
    path('search/<str:name>', views.search, name='search'),
    # path('SearchList/<str:name>/', SearchList.as_view()),
    url('^SearchList/(?P<name>.+)/$', SearchList.as_view()),
]