from django.urls import path, include
from . import views

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('category/<str:name>', views.CategoryDetailUpdateDeleteView.as_view(), name='author_detail'),
]
