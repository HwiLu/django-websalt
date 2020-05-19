from django.db import models

# Create your models here.

class Os(models.Model):
    os_version = models.CharField(max_length=64)
    os_num = models.CharField(max_length=16)

    def __str__(self):
        return self.os_version