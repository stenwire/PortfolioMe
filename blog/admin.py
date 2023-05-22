from django.contrib import admin

from backend.admin import admin_site
from blog.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    list_filter = ("status", "created_on", "updated_on")
    search_fields = (
        "title",
        "status",
        "content",
    )
    prepopulated_fields = {"slug": ("title",)}


admin_site.register(Article, ArticleAdmin)
