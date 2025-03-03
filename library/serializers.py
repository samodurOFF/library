from django.utils import timezone
from rest_framework import serializers
from .models import Book, Author, Member, Library, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publish_date']
        read_only_fields = ['publish_date']


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    libraries = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    current_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        # Использование параметра include_related из контекста
        representation = super().to_representation(instance)
        representation['current_time'] = self.context.get('current_time', None)
        return representation


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_date']
