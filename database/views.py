from django.shortcuts import render, get_object_or_404
from .models import Devices, Companies

# Create your views here.
def tablePage(request):
    # devices = get_object_or_404(Devices, pk=1)
    # devices = Devices.objects.filter(device_id='PL02')
    
    companies = Companies.objects.filter(company_name='MCI')
    devices = Devices.objects.filter(company_name__company_name="Nobka")
    # devices = Devices.objects.filter(device_id="PL01")
    # devices = Devices.objects.filter(company_name='Nobka')
    # devices = Devices.objects.filter(company_name_id=pk)
    # devices = Devices.objects.filter(company_name=companies)
    # print('+++++++++++++++++++++++++'+str(devices)+'+++++++++++++++++++++++++++++++')
    # devices = Devices.objects.exclude(id=company_name.id).filter(companies.company_name)
    # devices = Devices.objects.all()[1:3]
    # devices = Devices.objects.all()
    # for report in devices:
    #     devices.objects.filter(report.company_name.company_name='Nobka')
        # print('ID: {} Name: {}'.format(report.company_name.pk, report.company_name.company_name))
    context = {
        'devices': devices,
        'companies': companies
    }
    return render(request, 'table.html', context)