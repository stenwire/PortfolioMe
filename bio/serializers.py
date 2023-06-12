from rest_framework import serializers

from bio.models.bio import Bio
from bio.models.education import Education
from bio.models.experience import Experience
from bio.models.portfolio import Portfolio

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields = "__all__"
        lookup_fields = "pk"
        read_only_fields = ("pk","uuid")
        extra_kwargs = {
            "url": {"lookup_field": ("pk")},
        }


class BioSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Bio

class EducationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Education


class ExperienceSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Experience


class PortfolioSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Portfolio


class ServicesSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Portfolio

class SkillsSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Portfolio