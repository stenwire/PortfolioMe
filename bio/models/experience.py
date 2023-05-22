from django.db import models


class Experience(models.Model):
    position = models.CharField(
        max_length=200, verbose_name="Position"
    )
    company = models.CharField(
        max_length=200, verbose_name="Company"
    )
    location = models.CharField(
        max_length=200, verbose_name="Location"
    )
    started_on = models.DateField(
        max_length=200, verbose_name="Started on"
    )
    ended_on = models.DateField(
        max_length=200, verbose_name="Ended on", blank=True, default="Present"
    )

    class Meta:
        ordering = ["-started_on"]

    def __str__(self) -> str:
        return f"{self.position} - {self.company}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)