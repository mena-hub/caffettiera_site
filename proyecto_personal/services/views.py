from django.shortcuts import render
from .models import Service

def services(request):
    services = Service.objects.all()[::-1]
    return render(request, "services/services.html", 
                    {
                        'services':services
                        })