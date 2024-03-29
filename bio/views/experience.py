from rest_framework import generics, permissions

from bio.models.experience import Experience
from bio.serializers import ExperienceSerializer


class ListCreateExperienceAPIView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = "__all__"
    queryset = Experience.objects.all()


class RetrieveUpdateDestroyExperienceAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ExperienceSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Experience.objects.all()
