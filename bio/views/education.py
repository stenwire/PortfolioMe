from rest_framework import generics, permissions

from bio.models.education import Education
from bio.serializers import EducationSerializer


class ListCreateEducationAPIView(generics.ListCreateAPIView):
    serializer_class = EducationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = "__all__"
    queryset = Education.objects.all()


class RetrieveUpdateDestroyEducationAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = EducationSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Education.objects.all()
