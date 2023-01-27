# Service python sdk documentation
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_service

from django.db import models
from django.contrib import admin

from aws.models.loadbalancer import AWSLoadBalancer
from aws.use_cases.create_ecs_service import create_ecs_service


class AWSECSService(models.Model):

    # Service information
    name = models.CharField(max_length=30)
    desired_count = models.IntegerField(default=0)
    launch_type = "EC2"

    # Load balancer associations
    # ? Or public and private and no more ? .. it was a test for many to many
    load_balancers = models.ManyToManyField(AWSLoadBalancer, blank=True)

    # Where is service deployed
    cluster_name = models.CharField(max_length=30)

    # Used to change displayed name on lists or tables
    def __str__(self):
        return self.name

    # Used to change class name on the side bar
    class Meta:
        verbose_name = "ECS Service"
        verbose_name_plural = "ECS Services"


class AWSECSServiceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        if change:
            pass
        else:
            create_ecs_service()
        super().save_model(request, obj, form, change)


admin.site.register(AWSECSService, AWSECSServiceAdmin)
