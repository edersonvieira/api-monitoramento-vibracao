from rest_framework import serializers
from api.models import *

class DispositivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'

class ReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'