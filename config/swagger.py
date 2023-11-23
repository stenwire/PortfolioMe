from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Portfolio API",
        default_version="v1",
        description="Portfolio API",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="nwankwostephen039@yahoo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
