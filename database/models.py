from django.db import models

# Create your models here.

class Companies(models.Model):
    company_name = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name


class Devices(models.Model):
    device_id = models.CharField(max_length=50, verbose_name="id")
    device_ip = models.CharField(max_length=50, verbose_name="ip")
    company_name = models.ForeignKey(Companies, on_delete=models.CASCADE, default="", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.device_id


