from django.db import models


#Create your models here.
class SoftwareRoles(models.Model):
    testing = models.CharField(max_length=30)
    developing = models.CharField(max_length=30)
    sales = models.CharField(max_length=20)
    maintaining = models.CharField(max_length=30)

    def __str__(self):
        return self.developing
