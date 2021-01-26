from rest_framework import fields, serializers
from .models import Author, AuthorContainer, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    book_set = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = '__all__'

class AuthorContainerSerializer(serializers.ModelSerializer):
    author_set = AuthorSerializer(many=True)
    class Meta:
        model = AuthorContainer
        fields = '__all__'
