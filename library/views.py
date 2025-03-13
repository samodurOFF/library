from django.db.models import Count
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from library.models import Book, Author, Category
from library.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, AuthorSerializer, \
    CategorySerializer
from rest_framework.pagination import PageNumberPagination


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    pagination_class = PageNumberPagination
    page_size = 5

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'publish']
    search_fields = ['title', 'author__firstname', 'author__lastname']
    ordering_fields = ['publish_date']

    def get_page_size(self, request):
        page_size = request.query_params.get('page_size')
        if page_size and page_size.isdigit():
            return int(page_size)
        return self.page_size

    def get_queryset(self):
        page_size = self.get_page_size(self.request)
        self.pagination_class.page_size = page_size
        year = self.request.query_params.get('year')
        queryset = super().get_queryset()
        if year:
            queryset = queryset.filter(publish_date__year=year)

        return queryset.order_by('pk')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer
        elif self.request.method == 'GET':
            return BookListSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_time'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        return context


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

