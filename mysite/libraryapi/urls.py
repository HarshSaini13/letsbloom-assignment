from django.urls import path
from .views import BookDetail, BookList

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('<int:book_id>/', BookDetail.as_view(), name='book-detail'),
]
