from django.db import models

from utils.models import TrackObjectStateMixin


class Bio(TrackObjectStateMixin):
    firstname = models.CharField(max_length=200, verbose_name="First Name")
    lastname = models.CharField(max_length=200, verbose_name="Last Name")
    short_bio = models.TextField(max_length=250, verbose_name="Short Bio")
    long_bio = models.TextField(max_length=1000, verbose_name="Long Bio")
    email = models.EmailField(max_length=200, verbose_name="Email")
    github = models.URLField(max_length=200, blank=True, verbose_name="Github")
    twitter = models.URLField(
        max_length=200, blank=True, verbose_name="Twitter"
    )
    linkedin = models.URLField(
        max_length=200, blank=True, verbose_name="Linkedin"
    )
    phone = models.CharField(max_length=10, verbose_name="Phone")
    address = models.CharField(max_length=200, verbose_name="Address")

    def __str__(self) -> str:
        return f"{self.firstname} - {self.lastname}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
