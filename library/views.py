from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from .models import Book
from .serializers import BookSerializer

class BookView(APIView):

    def get(self, request):
            all_books = Book.objects.all()
            serializers = BookSerializer(all_books, many=True)
            filter_backends = [SearchFilter]
            search_fields = ['title']
            return Response(serializers.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    
class BookDetailView(APIView):
    
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise HTTP_404_NOT_FOUND

    def get(self, request, pk):
            book = self.get_object(pk)
            serializer_book = BookSerializer(book, many=False)
            return Response(serializer_book.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=HTTP_204_NO_CONTENT)