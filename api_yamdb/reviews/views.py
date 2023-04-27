from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Title
from users.permissions import IsModeratorAdminAuthorOrReadOnly

from .models import Comment, Review
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    Возвращает или создает отзыв к произведениям пользователей.
    """
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsModeratorAdminAuthorOrReadOnly
    )
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return Review.objects.filter(title=self.kwargs.get('title_id'))

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Возвращает или создает комментарий к отзывам пользователей.
    """
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsModeratorAdminAuthorOrReadOnly
    )
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return Comment.objects.filter(
            title=self.kwargs.get('title_id'),
            review=self.kwargs.get('review_id')
        )

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(
            author=self.request.user,
            title=title,
            review=review
        )
