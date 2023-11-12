from django.contrib import admin
from . import models


@admin.register(models.MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    fields = ["name", "file", "desc", "date"]
