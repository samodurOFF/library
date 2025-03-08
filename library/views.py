

from django.utils import timezone

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from library.models import Book, Category
from library.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    pagination_class = PageNumberPagination
    page_size = 5
    filter_backends = [
        DjangoFilterBackend, # filterset_fields
        filters.SearchFilter, # search_fields
        filters.OrderingFilter, # ordering_fields
    ]

    filterset_fields = [
        'author',
        'publish_date',
    ]

    search_fields = [
        'title',
        'author__lastname',
    ]
    ordering_fields = [
        'publish_date',
        'author__birth_date',
    ]

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

    def create(self, request, *args, **kwargs):
        books_data = request.data.copy()
        if not books_data.get('author'):
            books_data['author'] = 1
        serializer = self.get_serializer(data=books_data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer




class CategoryView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['current_time'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        return context

