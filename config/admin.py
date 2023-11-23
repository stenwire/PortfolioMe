from django.contrib import admin

# from blog.models import Article


class BlogAdminSite(admin.AdminSite):
    site_header = "Portfolio Administration"
    site_title = "Portfolio"
    index_title = "Portfolio Administration"
    empty_value_display = "- - - -"


admin_site = BlogAdminSite(name="Portfolio Admin Site")
