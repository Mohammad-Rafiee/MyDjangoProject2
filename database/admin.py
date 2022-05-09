from django.contrib import admin
from .models import Devices, Companies, Hotel

# Register your models here.
admin.site.register(Devices)
admin.site.register(Companies)
admin.site.register(Hotel)