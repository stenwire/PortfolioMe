from django.urls import path

from blog import views

urlpatterns = [
    path(
        "articles/",
        views.ListCreateArticleAPIView.as_view(),
        name="list-and-create-article-view",
    ),
    path(
        "articles/<uuid:uuid>/",
        views.RetrieveUpdateDestroyArticleAPIView.as_view(),
        name="read-update-delete-article-view",
    ),
    path("tags/", views.ListCreateTagAPIView.as_view(), name="tag-list"),
    path(
        "tags/<int:pk>/",
        views.RetrieveUpdateDestroyTagAPIView.as_view(),
        name="tag-detail",
    ),
]
