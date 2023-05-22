from django.contrib import admin

from backend.admin import admin_site
from bio.models.bio import Bio
from bio.models.education import Education
from bio.models.experience import Experience

# Register your models here.


class BioAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email")


class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "school", "location", "started_on", "ended_on")


class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "location",
        "started_on",
        "ended_on",
    )


admin_site.register(Bio, BioAdmin)
admin_site.register(Education, EducationAdmin)
admin_site.register(Experience, ExperienceAdmin)
