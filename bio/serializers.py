from utils.serializers import BaseSerializer

from .models.bio import Bio
from .models.education import Education
from .models.experience import Experience
from .models.portfolio import Portfolio
from .models.services import Service
from .models.skills import Skill


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
        model = Service


class SkillsSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Skill
