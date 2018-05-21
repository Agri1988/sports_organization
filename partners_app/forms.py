from django import forms
from django.db.models import Q

from .models import Client, Employee, IdentityDocument, AbstractPartner


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        using_identity_document = [obj.identity_document.id for obj in AbstractPartner.objects.filter(identity_document_id__isnull=False)]
        if not self.instance.identity_document:
            self.fields['identity_document'].queryset = IdentityDocument.objects.exclude(id__in=using_identity_document)
        else:
            self.fields['identity_document'].queryset = IdentityDocument.objects.filter(id=self.instance.identity_document.id)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        using_identity_document = [obj.identity_document.id for obj in AbstractPartner.objects.filter(identity_document_id__isnull=False)]
        self.fields['identity_document'].queryset = IdentityDocument.objects.exclude(id__in=using_identity_document)



# class IdentityDocumentForm(forms.ModelForm):
#     class Meta:
#         model = IdentityDocument
#         fields = "__all__"