from django.shortcuts import render, get_object_or_404, redirect
from .models import Devices, Companies
from django.http import HttpResponse
from .forms import HotelForm
from .models import Hotel

# Create your views here.
def tablePage(request):
    
    companies = Companies.objects.filter(company_name='MCI')
    devices = Devices.objects.filter(company_name__company_name="Nobka")
 
    # devices = Devices.objects.all()
    # for report in devices:
    #     devices.objects.filter(report.company_name.company_name='Nobka')
        # print('ID: {} Name: {}'.format(report.company_name.pk, report.company_name.company_name))
    context = {
        'devices': devices,
        'companies': companies
    }
    return render(request, 'table.html', context)

def categories(request, slug):
    category = get_object_or_404(Devices, slug)

def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm
    
    return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

def display_hotel_images(request, id):
    
    if request.method == 'GET':
        # hotels = Hotel.objects.all()
        hotels = Hotel.objects.get(id=id)
        return render(request, 'display_hotel_images.html',
                    {'hotel_images':hotels})