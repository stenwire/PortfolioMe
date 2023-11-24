from django.contrib import admin

from blog.models import Article
from config.admin import admin_site

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_on")
    list_filter = ("status", "created_on", "updated_on")
    search_fields = (
        "title",
        "status",
        "content",
    )
    readonly_fields = ("uuid",)
    prepopulated_fields = {"slug": ("title",)}


admin_site.register(Article, ArticleAdmin)
