from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name='index'),
    path("about/", views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('services/', views.Service, name='services'),
    path("transit-agency/", views.Transit_Agency, name='transit'),
    path("port-agency/", views.Port_Agency, name='port'),
    path("shipyard-agency/", views.Shipyard_Agency, name='shipyard'),
    path("husbandry-agency/", views.Husbandry_Agency, name='husbandry'),
    path('service/<slug:slug>', views.Service_Detail, name='service_detail'),
]
