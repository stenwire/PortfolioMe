from django.contrib import admin

from bio.models.bio import Bio
from bio.models.education import Education
from bio.models.experience import Experience
from bio.models.portfolio import Portfolio
from bio.models.services import Service
from bio.models.skills import Skill
from config.admin import admin_site

# Register your models here.


class BioAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email")
    readonly_fields = ("uuid",)


class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "location", "started_on", "ended_on")
    readonly_fields = ("uuid",)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "location",
        "started_on",
        "ended_on",
    )
    readonly_fields = ("uuid",)


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ("uuid",)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    readonly_fields = ("uuid",)


class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "location", "started_on", "ended_on")
    readonly_fields = ("uuid",)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "tag",
        "title",
        "link",
    )
    readonly_fields = ("uuid",)


admin_site.register(Bio, BioAdmin)
admin_site.register(Education, EducationAdmin)
admin_site.register(Experience, ExperienceAdmin)
admin_site.register(Portfolio, PortfolioAdmin)
admin_site.register(Skill, SkillAdmin)
admin_site.register(Service, ServiceAdmin)
