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
    path(
        "articles/admin/",
        views.ListUserArticleAPIView.as_view(),
        name="list-articles-by-user-view",
    ),
]
