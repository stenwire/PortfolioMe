from rest_framework import generics, permissions

from bio.models.services import Service
from bio.serializers import ServicesSerializer


class ListCreatePortfolioAPIView(generics.ListCreateAPIView):
    serializer_class = ServicesSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = "__all__"
    queryset = Service.objects.all()


class RetrieveUpdateDestroyPortfolioAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ServicesSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Service.objects.all()
