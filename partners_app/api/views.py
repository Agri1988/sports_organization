from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from partners_app.api.serializers import SerializerClient, SerializerEmployee, SerialazerIdentityDocument
from ..models import Client, Employee, IdentityDocument



# Create your views here.

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SerializerClient


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = SerializerEmployee


class IdentityDocumentViewSet(ModelViewSet):
    queryset = IdentityDocument.objects.all()
    serializer_class = SerialazerIdentityDocument

