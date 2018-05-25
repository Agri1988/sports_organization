"""sports_organization URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from . import views
from .models import Client, Employee, IdentityDocument
from .forms import ClientForm, EmployeeForm

app_name = 'partners_app'




urlpatterns = [
    path('api/', include('partners_app.api.urls')),

    path('client_list/', views.ClientListView.as_view(), name='client_list'),
    path('employee_list/', views.EmployeeListView.as_view(), name='employee_list'),
    path('new_client/', views.ClientCreateView.as_view(), name='new_client'),
    path('detail_client/<int:pk>/', views.ClientUpdateView.as_view(), name='detail_client'),
    path('new_employee/', views.EmployeeCreateView.as_view(), name='new_employee'),
    path('detail_employee/<int:pk>/', views.EmployeeUpdateView.as_view(), name='detail_employee'),
    path('delete_employee/<int:pk>/', views.EmployeeDeleteView.as_view(),name='delete_employee'),
    path('delete_client/<int:pk>/', views.ClientDeleteView.as_view(), name='delete_client'),
    path('get_identity_document_form/', views.GetIdentityDocumentForm.as_view(),name='new_identity_document'),
]
