from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from rest_framework.viewsets import ModelViewSet

from partners_app.api.serializers import SerializerClient
from partners_app.forms import EmployeeForm, ClientForm
from .models import Client, Employee, IdentityDocument
from .utils import get_data_to_field


# Create your views here.

class PartnersListView(ListView):
    template_name = 'partners_app/partners_list.html'
    context_object_name = 'partners'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PartnersListView, self).get_context_data(**kwargs)
        context['partner_type'] = str(self.model).split('.')[-1][:-2].lower()
        return context


class ClientListView(PartnersListView):
    model = Client


class EmployeeListView(PartnersListView):
    model = Employee


class PartnerCreateView(CreateView):
    template_name = 'partners_app/detail_partner.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerCreateView, self).get_context_data(**kwargs)
        context['partner_type'] = str(self.model).split('.')[-1][:-2].lower()
        return context


class ClientCreateView(PartnerCreateView):
    model = Client
    form_class = ClientForm


class EmployeeCreateView(PartnerCreateView):
    model = Employee
    form_class = EmployeeForm


class PartnerUpdateView(UpdateView):
    template_name = 'partners_app/detail_partner.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PartnerUpdateView, self).get_context_data(*args, **kwargs)
        partner_type = str(self.model).split('.')[-1][:-2].lower()
        context['partner_type'] = partner_type
        return context


class ClientUpdateView(PartnerUpdateView):
    model = Client
    form_class = ClientForm

class EmployeeUpdateView(PartnerUpdateView):
    model = Employee
    form_class = EmployeeForm


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('partners_app:client_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('partners_app:employee_list')

class GetIdentityDocumentForm(CreateView):
    model = IdentityDocument
    fields = '__all__'
    template_name= 'partners_app/snippets/form_snippet.html'