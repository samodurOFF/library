from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryDetailUpdateDeleteView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register(r'categories', CategoryDetailUpdateDeleteView)
urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('user_book_detail', views.UserListView.as_view(), name='user_book_detail'),
    path('', include(router.urls), name='category_detail'),
    path('oauth/', obtain_auth_token, name='auth_token'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-obtain/', TokenObtainPairView.as_view(), name='token_obtain'),
]
