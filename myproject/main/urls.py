"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='index'),
    path('', views.index, name='index'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('portfolio-details2/', views.portfolio_details2, name='portfolio-details2'),
    path('portfolio-details3/', views.portfolio_details3, name='portfolio-details3'),
    path('sarter-page/', views.sarter_page, name='sarter-page'),
    path('service-details/', views.service_details, name='service-details'),
    path('service-details2/', views.service_details, name='service-details2'),
    path('service-details3/', views.service_details, name='service-details3'),
    path('service-details4/', views.service_details, name='service-details4'),
    path('service-details5/', views.service_details, name='service-details5'),
    path('service-details6/', views.service_details, name='service-details6'),
    path('api/contact/', views.ContactView.as_view(), name='contact'),  # Added trailing slash
]