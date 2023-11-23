from django.db import models

from utils.models import TrackObjectStateMixin


class Service(TrackObjectStateMixin):
    name = models.CharField(max_length=200, verbose_name="Name")
    cover_image = models.URLField(
        max_length=200, blank=True, verbose_name="Cover Image"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
