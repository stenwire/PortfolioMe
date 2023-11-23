from rest_framework import generics, permissions

from bio.models.skills import Skill
from bio.serializers import SkillsSerializer


class ListCreatePortfolioAPIView(generics.ListCreateAPIView):
    serializer_class = SkillsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = "__all__"
    queryset = Skill.objects.all()


class RetrieveUpdateDestroyPortfolioAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = SkillsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Skill.objects.all()
