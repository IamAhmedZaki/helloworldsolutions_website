from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def sarter_page(request):
    return render(request, 'sarter-page.html')

def service_details(request):
    return render(request, 'service-details.html')