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
from .models import Client, Employee, PartnerPhoto, IdentityDocument
from .forms import ClientForm, EmployeeForm

app_name = 'partners_app'




urlpatterns = [
    path('client_list/', views.PartnersListView.as_view(**{'model':Client}), name='client_list'),
    path('employee_list/', views.PartnersListView.as_view(**{'model':Employee}), name='employee_list'),
    path('new_client/', views.PartnerCreateView.as_view(**{'form_class':ClientForm,'model':Client}),name='new_client'),
    path('detail_client/<int:pk>/', views.PartnerUpdateView.as_view(**{'form_class':ClientForm,'model':Client}),
         name='detail_client'),
    path('new_employee/', views.PartnerCreateView.as_view(**{'form_class':EmployeeForm,'model':Employee}),
         name='new_employee'),
    path('detail_employee/<int:pk>/', views.PartnerUpdateView.as_view(
        **{'form_class':EmployeeForm,'model':Employee}),name='detail_employee'),
    path('delete_employee/<int:pk>/', DeleteView.as_view(
        **{'model':Employee, 'success_url':reverse_lazy('partners_app:employee_list')}),name='delete_employee'),
    path('delete_client/<int:pk>/', DeleteView.as_view(
        **{'model':Client, 'success_url':reverse_lazy('partners_app:client_list')}),name='delete_client'),
    path('delete_image/<int:pk>/', views.DeleteImageView.as_view(
        **{'model':PartnerPhoto}),name='delete_photo'),
    # path('new_identity_document/', views.CreateView.as_view(**{'model':IdentityDocument, 'fields':'__all__',
    #     'template_name':'partners_app/snippets/form_snippet.html', 'success_url':False}),name='new_identity_document'),
    path('ajax_form/', views.AjaxView.as_view(**{'model':IdentityDocument, 'fields':'__all__',
        'template_name':'partners_app/snippets/form_snippet.html'}),name='new_identity_document'),
]
