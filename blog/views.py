from django.utils import timezone
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from blog.models import Article, Tag
from blog.serializers import ArticleSerializer, TagSerializer


class ListCreateArticleAPIView(generics.ListCreateAPIView):
    """
    This view is used to:
        1. create a new article
        2. list all articles that have been published
    ...
    """

    queryset = Article.objects.filter(status="1")
    serializer_class = ArticleSerializer
    filterset_fields = ["title", "tags"]
    # permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDestroyArticleAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    """
    This view is used to:
        1. Read an article
        2. Update an article
        3. Delete an article
    ...
    """

    serializer_class = ArticleSerializer
    lookup_field = "uuid"
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.all()


class ListCreateTagAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class RetrieveUpdateDestroyTagAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
