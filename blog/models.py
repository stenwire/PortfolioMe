from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls.base import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils.models import TrackObjectStateMixin

STATUS = ((0, "Draft"), (1, "Publish"))


class Tag(TrackObjectStateMixin):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return "Tag[id: {id}, name: {name}]".format(id=self.id, name=self.name)

    def get_absolute_url(self):
        return reverse(
            "blog:tag-detail",
            kwargs={"uuid": self.uuid},
        )


class Article(TrackObjectStateMixin):
    title = models.CharField(max_length=200, unique=True, verbose_name="Title")
    subtitle = models.TextField(max_length=150, blank=True)
    tags = models.ManyToManyField(Tag, related_name="articles")
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    cover_image = models.URLField(_("URL to image"), max_length=200)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        verbose_name="Author",
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(_("Content"))
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=STATUS, default=0, verbose_name="Status"
    )
    published_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, verbose_name="Published Date"
    )

    OWNER_FIELD = "author"

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.status = "published"
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "blog:article-detail",
            kwargs={"slug": self.slug, "uuid": self.uuid},
        )
