from django.contrib import admin
from .models import FileUpload, Service, WebsiteInfo


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "id", "file",
    )


@admin.register(WebsiteInfo)
class WebsiteInfoAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "id", "website",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
        "id", "model_version",
    )
