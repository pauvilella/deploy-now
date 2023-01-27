# Service python sdk documentation
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_service

from django.db import models
from django.contrib import admin


class AWSECSService(models.Model):

    # Service information
    service_name = models.CharField(max_length=30)

    # Where is service deployed
    cluster_name = models.CharField(max_length=30)

    # Used to change class name
    class Meta:
        verbose_name = "ECS Service"
        verbose_name_plural = "ECS Services"


class AWSECSServiceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        print(change)  # IS new or not the saved model
        super().save_model(request, obj, form, change)


admin.site.register(AWSECSService, AWSECSServiceAdmin)
