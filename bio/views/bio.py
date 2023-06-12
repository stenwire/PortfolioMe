from rest_framework import generics, permissions

from bio.models.bio import Bio
from bio.serializers import BioSerializer


class ListCreateBioAPIView(generics.ListCreateAPIView):
    serializer_class = BioSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = "__all__"
    queryset = Bio.objects.all()


class RetrieveUpdateDestroyBioAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BioSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bio.objects.all()
