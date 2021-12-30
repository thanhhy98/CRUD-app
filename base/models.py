from django.db import models


# Create your models here.

class WebForm(models.Model):
    tenhang = models.CharField(max_length=200, null=True)
    dvt = models.CharField(max_length=200, null=True)
    soluong = models.CharField(max_length=200, null=True)
    dongia = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.tenhang
