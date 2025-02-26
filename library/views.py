from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from library.models import Book
from library.serializers import BookListSerializer, BookDetailSerializer, BookCreateSerializer


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookDetailSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['POST'])
def book_create(request):
    serializer = BookCreateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)