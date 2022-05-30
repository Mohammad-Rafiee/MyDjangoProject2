from django.shortcuts import render, get_object_or_404, redirect
from .models import Devices, Companies
from django.http import HttpResponse
from .forms import HotelForm, DataForm, ContactForm, DeviceConfigForm
from .models import Hotel
from django.views.generic.edit import FormView
# from django.

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
        form = HotelForm()
    
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

# class DataForm(MultiFormsView):

def contactPage(request):
    form = ContactForm()
    context ={
        'form': form,
    }
    return render(request, 'dataform.html', context)

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

def deviceForm(request, id):
    if request.method == 'POST':
        form = DeviceConfigForm(request.POST)
        if form.is_valid():
            # create = DeviceModel.objects.create(DeviceConfigForm)
            # try:
            # form.save()
            # except IntegrityError:
            ssid = form.cleaned_data['ssid']
            password = form.cleaned_data['password']
            device_ip = form.cleaned_data['device_ip']
            broker_ip = form.cleaned_data['broker_ip']
            gateway = form.cleaned_data['gateway']
            subnet = form.cleaned_data['subnet']
            port = form.cleaned_data['port']
            mqtt_username = form.cleaned_data['mqtt_username']
            mqtt_password = form.cleaned_data['mqtt_password']
            
            reg = Devices(ssid=ssid, password=password, device_ip=device_ip, broker_ip=broker_ip, gateway=gateway, subnet=subnet, port=port, mqtt_username=mqtt_username, mqtt_password=mqtt_password)
            reg.save()

            # publish.single(send_topic, 'cli', hostname=broker_address, auth = {'username':user, 'password':password})
            # form.save()
            return redirect('tablePage')
    else:
        form = DeviceConfigForm()

    context = {
        'form': form,
    }

    return render(request, 'deviceform.html', context)