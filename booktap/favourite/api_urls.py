from django.urls import path
from favourite import views
from favourite.views import SingleUserFavoriteListView

urlpatterns = [
    path('getwishlist/', views.getwishlist, name='getwishlist'),
    path('postwishlist/', views.postwishlist, name='postwishlist'),
    # path('CustomerWishListView/<int:id>/', CustomerWishListView.as_view()),
    path('SingleUserFavoriteListView/<int:id>/', SingleUserFavoriteListView.as_view()),
]