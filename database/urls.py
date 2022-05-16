from django.urls import path
from . import views

urlpatterns = [
    path('table', views.tablePage, name='tablePage'),
    path('image_upload', views.hotel_image_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('<id>/hotel_images', views.display_hotel_images, name='hotel_images'),
    # path('<slug:slug>', views.categories, name='category_products'),
    path('names', views.company_names, name='company_name'),
    path('names_to_devices/<id>', views.names_to_devices, name='names_to_devices'),
]