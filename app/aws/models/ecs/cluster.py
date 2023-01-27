# Cluster python sdk documentation
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_cluster

from django.db import models
from django.contrib import admin


class AWSECSCluster(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # Used to change class name
    class Meta:
        verbose_name = "ECS Cluster"
        verbose_name_plural = "ECS Clusters"


class AWSECSClusterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        print(change)  # IS new or not the saved model
        super().save_model(request, obj, form, change)


admin.site.register(AWSECSCluster, AWSECSClusterAdmin)
