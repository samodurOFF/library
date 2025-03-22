from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('category', views.CategoryView)

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('', include(router.urls), name='category_family'),

]


