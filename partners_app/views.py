from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.core.exceptions import ObjectDoesNotExist
from .models import PartnerPhoto
from .utils import add_image_to_model, get_data_to_field

# Create your views here.

class PartnersListView(ListView):
    template_name = 'partners_app/partners_list.html'
    context_object_name = 'partners'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        return super(PartnersListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PartnersListView, self).get_context_data(**kwargs)
        context['partner_type'] = str(self.model).split('.')[-1][:-2].lower()
        return context


class PartnerCreateView(CreateView):
    template_name = 'partners_app/detail_partner.html'

    def get_context_data(self, **kwargs):
        context = super(PartnerCreateView, self).get_context_data(**kwargs)
        context['partner_type'] = str(self.model).split('.')[-1][:-2].lower()
        return context

    def post(self, request, *args, **kwargs):
        super(PartnerCreateView, self).post(request, *args,**kwargs)
        return HttpResponseRedirect(reverse('partners_app:%s_list' % str(self.model).split('.')[-1][:-2].lower()))


class PartnerUpdateView(UpdateView):
    template_name = 'partners_app/detail_partner.html'
        
    def get_context_data(self, *args, **kwargs):
        context = super(PartnerUpdateView, self).get_context_data(*args, **kwargs)
        context['partner_type'] = str(self.model).split('.')[-1][:-2].lower()
        try:
            context['image'] = PartnerPhoto.objects.get(partner_id=self.kwargs['pk'])
        except ObjectDoesNotExist:
            context['image'] = None
        return context

    def post(self, request, *args, **kwargs):
        if request.FILES:
            add_image_to_model(request.FILES['image'], PartnerPhoto, 'partner', self.model.objects.get(id=kwargs['pk']))
        super(PartnerUpdateView, self).post(request, *args,**kwargs)
        return HttpResponseRedirect(reverse('partners_app:%s_list' % str(self.model).split('.')[-1][:-2].lower()))


class DeleteImageView(DeleteView):
    def get(self, request, *args, **kwargs):
        self.model.objects.get(id=kwargs['pk']).delete()
        return HttpResponseRedirect(request.GET['url'])


class AjaxView(CreateView):
    def post(self, request, *args, **kwargs):
        return JsonResponse(get_data_to_field(self.get_form_class(), self.model, request))
