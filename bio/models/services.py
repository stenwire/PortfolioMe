from django.db import models
from utils.models import TrackObjectStateMixin


class Services(TrackObjectStateMixin):
    name = models.CharField(max_length=200, verbose_name="Name")

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
