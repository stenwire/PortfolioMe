from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from blog.models import Article
from blog.serializers import ArticleSerializer


class ListCreateArticleAPIView(generics.ListCreateAPIView):
    """
    This view is used to:\n
        1. create a new article
        2. list all articles that have been published
    ...

    The user needs to be authenticated either by normal log-in or with api key
    """

    queryset = Article.objects.filter(status="1")
    serializer_class = ArticleSerializer
    filterset_fields = "__all__"
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDestroyArticleAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to:\n
        1. Read an article
        2. Update an article
        3. Delete an article
    ...

    The user needs to be authenticated either by normal log-in or with api key
    """
    serializer_class = ArticleSerializer
    lookup_field = "uuid"
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ListUserArticleAPIView(generics.ListAPIView):
    """
    This view is used to list all articles by a user
    ...

    The user needs to be an admin and authenticated by normal log-in
    """

    serializer_class = ArticleSerializer
    filterset_fields = "__all__"
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
