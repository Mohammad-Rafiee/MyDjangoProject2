from django.shortcuts import render, get_object_or_404, redirect
from .models import Devices, Companies
from django.http import HttpResponse
from .forms import HotelForm, DataForm
from .models import Hotel

# Create your views here.
def tablePage(request):
    
    companies = Companies.objects.filter(company_name='MCI')
    # devices = Devices.objects.filter(company_name__company_name="Nobka")
 
    devices = Devices.objects.all()
    # for report in devices:
    #     devices.objects.filter(report.company_name.company_name='Nobka')
        # print('ID: {} Name: {}'.format(report.company_name.pk, report.company_name.company_name))
    context = {
        'devices': devices,
        'companies': companies
    }
    return render(request, 'table.html', context)

# def categories(request, slug):
#     category = get_object_or_404(Devices, company_name__company_name=slug)
#     companies = Companies.objects.filter(is_active=True, category=category)
#     categories = Devices.objects.filter(is_active=True)

#     context={
#         'category': category,
#         'companies': companies,
#         'categories': categories,
#     }
#     return render(request, 'category_products.html', context)


def company_names(request):
    companies = Companies.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'company_name.html', context)


def names_to_devices(request, id):
    devices = Devices.objects.filter(company_name=id)
    context = {
        'devices': devices
    }
    return render(request, 'table.html', context)



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

def data_form(request):

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            age = request.POST.get('age')
            return redirect('tablePage')

    form = DataForm()

    context = {
        'form': form
    }
    return render(request, 'dataform.html', context)