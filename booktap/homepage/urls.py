from django.urls import path
from homepage import views
from homepage.views import Profile

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<username>', Profile.as_view()),

]