from rest_framework import generics, permissions

from bio.models.services import Services
from bio.serializers import ServicesSerializer


class ListCreatePortfolioAPIView(generics.ListCreateAPIView):
    serializer_class = ServicesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = "__all__"
    queryset = Services.objects.all()


class RetrieveUpdateDestroyPortfolioAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ServicesSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Services.objects.all()
