from django.db import models
from django.contrib import admin


class AWSLoadBalancer(models.Model):

    name = models.CharField(max_length=50)
    arn = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Load balancer"
        verbose_name_plural = "Load balancers"


admin.site.register(AWSLoadBalancer)
