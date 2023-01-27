from django.db import models
from django.contrib import admin


class AWSLoadBalancer(models.Model):

    arn = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Load balancer"
        verbose_name_plural = "Load balancers"


admin.site.register(AWSLoadBalancer)
