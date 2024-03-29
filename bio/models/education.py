from django.db import models

from utils.models import TrackObjectStateMixin


class Education(TrackObjectStateMixin):
    degree = models.CharField(max_length=200, verbose_name="Degree")
    school = models.CharField(max_length=200, verbose_name="School")
    location = models.CharField(max_length=200, verbose_name="Location")
    started_on = models.DateField(max_length=200, verbose_name="Started on")
    ended_on = models.DateField(max_length=200, verbose_name="Ended on")
    school_logo = models.URLField(
        max_length=200, blank=True, verbose_name="Cover Image"
    )

    class Meta:
        ordering = ["-started_on"]

    def __str__(self) -> str:
        return f"{self.degree} - {self.school}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
