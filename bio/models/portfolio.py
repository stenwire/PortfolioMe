from django.db import models
from utils.models import TrackObjectStateMixin

TAG = (
    (0,"Website"),
    (1,"API"),
    (2,"Console")
)

class Portfolio(TrackObjectStateMixin):
    tag = models.IntegerField(choices=TAG, default=0, verbose_name="Tag")
    title = models.CharField(max_length=200, verbose_name="Title")
    body = models.TextField(max_length=250, verbose_name="Body")
    link = models.URLField(max_length=200, blank=True, verbose_name="Link")
    cover_image = models.URLField(
        max_length=200, blank=True, verbose_name="Cover Image"
    )
    published_on = models.DateField(max_length=200, verbose_name="Published on")

    class Meta:
        ordering = ["-published_on"]

    def __str__(self) -> str:
        return f"{self.tag} - {self.title}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
