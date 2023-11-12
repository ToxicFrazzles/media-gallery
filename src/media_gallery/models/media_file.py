from pathlib import Path

from django.conf import settings
from django.db import models


class MediaFile(models.Model):
    class MediaType:
        UNKNOWN = 0
        IMAGE = 1
        VIDEO = 2
    file = models.FileField(upload_to=(Path(settings.MEDIA_ROOT) / "media_gallery"))
    name = models.CharField(max_length=32)
    desc = models.TextField(blank=True, default="", verbose_name="Description")
    date = models.DateTimeField(auto_created=True)
