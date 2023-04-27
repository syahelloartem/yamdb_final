from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from reviews.models import Category, Genre, Title
from users.permissions import IsAdminOrReadOnly

from .filters import TitleFilter
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleGetSerializer, TitlePostSerializer)


class CreateListDeleteViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryViewSet(CreateListDeleteViewSet):
    """
    Возвращает или создает категорию произведения.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    search_fields = ('=name',)
    http_method_name = ('get', 'post', 'delete')


class GenreViewSet(CreateListDeleteViewSet):
    """
    Возвращает или создает жанр произведения.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'slug'
    search_fields = ('=name',)
    http_method_name = ('get', 'post', 'delete')


class TitleViewSet(viewsets.ModelViewSet):
    """
    Возвращает или создает произведение.
    """
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_class = TitleFilter
    search_fields = ('name', 'year', 'genre', 'category')
    http_method_name = ('get', 'post', 'patch', 'delete')

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TitleGetSerializer
        return TitlePostSerializer
