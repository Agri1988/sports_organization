from rest_framework import serializers

from partners_app.models import Client, IdentityDocument


class SerializerClient(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class SerializerEmployee(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

class SerialazerIdentityDocument(serializers.ModelSerializer):
    document_obj_name = serializers.SerializerMethodField()
    class Meta:
        model = IdentityDocument
        fields = '__all__'
    def get_document_obj_name(self, obj):
        return obj.__str__()