from django.urls import path, include
from . import views

urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('book_list/<int:pk>', views.book_detail, name='book_detail'),
    path('book_list/create', views.book_create, name='book_create'),
]
