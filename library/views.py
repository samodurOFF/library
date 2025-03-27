from django.db.models import Count
from django.template.context_processors import request
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from library.models import Book, Author, Category
from library.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, AuthorSerializer, \
    CategorySerializer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    # permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'publish']
    search_fields = ['title', 'author__firstname', 'author__lastname']
    ordering_fields = ['publish_date']

    def get_permissions(self):
        if self.request.method == 'GET':
            return super().get_permissions()
        return [IsAdminUser()]

    def filter_queryset(self, queryset):
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(publish_date__year=year)
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer
        elif self.request.method == 'GET':
            return BookListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_time'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        return context

class UserListView(ListAPIView):
    serializer_class = BookListSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)


class CategoryDetailUpdateDeleteView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=False, methods=['get'])
    def all_statistic(self, request):
        categories_with_book_counts = Category.objects.annotate(book_count=Count('books'))
        data = [
            {
                "id": category.id,
                "category": category.name,
                "book_count": category.book_count
            }
            for category in categories_with_book_counts
        ]
        return Response(data)

    @action(detail=True, methods=['get'])
    def statistic(self, request, pk=None):
        categories_with_book_counts = Category.objects.get(pk=pk)
        return Response(self.get_serializer(categories_with_book_counts).data)
