from rest_framework.generics import ListAPIView, CreateAPIView


from .serializer import BookModelSerializer
from main.models import Book


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer