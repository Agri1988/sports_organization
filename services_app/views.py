from django.shortcuts import render
from .models import Service

# Create your views here.
def services_list(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request, 'services_app/services_list.html', context)