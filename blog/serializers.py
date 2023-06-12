from rest_framework import serializers

from blog.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("uuid","slug")
        lookup_field = "uuid"
        extra_kwargs = {
            "url": {"lookup_field": ("uuid")},
        }
