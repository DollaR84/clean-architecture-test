from django.db import models

import uuid

from application.types import StatusType


class WebsiteInfo(models.Model):
    class Meta:
        db_table = "website_infos"
        verbose_name = "Site information"
        verbose_name_plural = "Information about sites"

    id = models.BigAutoField(primary_key=True)
    website = models.URLField(unique=True)
    emails = models.TextField()
    phones = models.TextField()


class FileUpload(models.Model):

    class Meta:
        db_table = "file_uploads"
        verbose_name = "Uploaded file"
        verbose_name_plural = "Uploaded files"

    id = models.BigAutoField(primary_key=True)
    filename = models.FileField(upload_to='uploads/', blank=True)


class Upload(models.Model):

    class Meta:
        db_table = "uploads"
        verbose_name = "Uploaded data"
        verbose_name_plural = "Uploaded data"

    id = models.BigAutoField(primary_key=True)
    uuid_id = models.UUIDField(unique=True, null=False, default=uuid.uuid4)

    urls = models.TextField(null=True)
    file = models.ForeignKey(
        "FileUpload",
        blank=True,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        verbose_name="Upload file",
    )

    status = models.CharField(
        max_length=12,
        choices=[(el, el.value) for el in StatusType],
        null=False, default=StatusType.NOT_STARTED,
        verbose_name="Status",
    )


class Service(models.Model):

    class Meta:
        db_table = "services"
        verbose_name = "Service"
        verbose_name_plural = "Services"

    id = models.BigAutoField(primary_key=True)
    model_version = models.CharField(max_length=100)

    @classmethod
    def get_current_version(cls):
        service = cls.objects.first()
        if service:
            return service.model_version
        else:
            return None
