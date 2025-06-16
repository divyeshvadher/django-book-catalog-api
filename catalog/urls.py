from django.urls import path
from .views import BookListView, BookDetailView, UploadCoverView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/<int:pk>/upload-cover/', UploadCoverView.as_view()),
]
