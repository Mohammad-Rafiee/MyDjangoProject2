from django.urls import path
from . import views

urlpatterns = [
    path('', views.tablePage, name='tablePage'),
    path('image_upload', views.hotel_image_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('<id>/hotel_images', views.display_hotel_images, name='hotel_images'),
]