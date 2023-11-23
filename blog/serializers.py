from rest_framework import serializers

from blog.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True, queryset=Tag.objects.all(), slug_field="text"
    )

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("uuid", "slug")
        lookup_field = "uuid"
        extra_kwargs = {
            "url": {"lookup_field": ("uuid")},
        }


class TagSerializer(serializers.ModelSerializer):
    articles = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Tag
        fields = "__all__"
