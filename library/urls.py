from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CategoryDetailUpdateDeleteView

router = DefaultRouter()
router.register(r'categories', CategoryDetailUpdateDeleteView)
urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('', include(router.urls), name='category_detail'),
]
