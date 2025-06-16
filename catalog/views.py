from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from .decorators import require_api_key
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(require_api_key)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @method_decorator(require_api_key)
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = self.serializer_class(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @method_decorator(require_api_key)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UploadCoverView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @method_decorator(require_api_key)
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        cover = request.FILES.get('cover')

        if not cover:
            return Response({"error": "NO_FILE", "message": "No file uploaded"}, status=400)

        if cover.content_type not in ['image/jpeg', 'image/png', 'image/webp']:
            return Response({
                "error": "INVALID_FILE_TYPE",
                "message": "Only JPG, PNG, and WEBP files are allowed",
                "allowed_types": ["jpg", "png", "webp"],
                "received_type": cover.content_type.split('/')[-1]
            }, status=400)

        if cover.size > 2 * 1024 * 1024:
            return Response({
                "error": "FILE_TOO_LARGE",
                "message": "Maximum allowed size is 2MB"
            }, status=413)

        book.cover_image = cover
        book.save()

        return Response({
            "id": book.id,
            "title": book.title,
            "cover_url": book.cover_image.url,
            "message": "Cover uploaded successfully"
        }, status=200)
