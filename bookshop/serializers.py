from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = 'all'

class BookSerializer(serializers.ModelSerializer):
    author_detail = AuthorSerializer(source='author', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_detail', 'isbn', 'price', 'stock', 'published_date', 'created_at']