from django.db import models

# Create your models here.

class Companies(models.Model):
    company_name = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name


class Devices(models.Model):
    device_id = models.CharField(max_length=50, verbose_name="ID")
    device_ip = models.CharField(max_length=50, verbose_name="IP")
    company_name = models.ForeignKey(Companies, on_delete=models.CASCADE, default="", null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Is Checked?', null=True)

    class Meta:
        verbose_name_plural = 'Devices'

    def __str__(self):
        return self.device_id

# models.py
class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='images/')

