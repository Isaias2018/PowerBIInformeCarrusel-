from django.shortcuts import render

def hola_mundo(request):
    return render(request, 'mi_app/hola_mundo.html')

def dashboard_power_bi(request):
    return render(request, 'mi_app/dashboard_power_bi.html')
