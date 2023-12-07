from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status
from myapp.models import Library
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LibrarySerializer

# Create your views here.
# class LibraryAPIView(generics.ListAPIView):
#     queryset = Library.objects.all()
#     serializer_class = LibrarySerializer
#
# class BookDetail(generics.RetrieveAPIView):
#     queryset = Library.objects.all()
#     serializer_class = LibrarySerializer

class BookList(APIView):
    def get(self, request):
        books = Library.objects.all()
        serializer = LibrarySerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            author = serializer.validated_data.get('author')

            if Library.objects.filter(name=name, author=author).exists():
                return Response({"error": "This book already exists."}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_book(self, book_id):
        try:
            return Library.objects.get(pk=book_id)
        except Library.DoesNotExist:
            raise Http404

    def put(self, request, book_id):
        book = self.get_book(book_id)
        serializer = LibrarySerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
