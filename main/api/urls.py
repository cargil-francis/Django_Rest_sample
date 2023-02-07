from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BookListView, BookCreateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create', BookCreateView.as_view(), name='book-create'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
