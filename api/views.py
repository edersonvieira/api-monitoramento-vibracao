from rest_framework import generics, permissions
from api.models import *
from api.serializers import *
from operator import itemgetter

dispositivo_config = {
    'queryset': Dispositivo.objects.all(),
    'serializer_class': DispositivosSerializer
}

reporte_config = {
    'queryset': Reporte.objects.all(),
    'serializer_class': ReportesSerializer
}

class DispositivoLC(generics.ListCreateAPIView):
    queryset, \
    serializer_class = itemgetter('queryset', 'serializer_class')(dispositivo_config)

    def get_queryset(self):
        return Dispositivo.objects.all()

class DispositivoRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset, \
    serializer_class = itemgetter('queryset', 'serializer_class')(dispositivo_config)

    def get_object(self):
        try:
            condicao = {}
            condicao['uid'] = self.kwargs["uid"]

            return Dispositivo.objects.get(**condicao)
        except Dispositivo.DoesNotExist:
            raise Dispositivo.NotFound(detail="Registro não encontrado", code=404)

class ReporteLC(generics.ListCreateAPIView):
    queryset, \
    serializer_class = itemgetter('queryset', 'serializer_class')(reporte_config)

    def get_queryset(self):
        condicao = {}
        condicao['id_dispositivo__uid'] = self.kwargs["uid"]
        return Reporte.objects.filter(**condicao)

class ReporteRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset, \
    serializer_class = itemgetter('queryset', 'serializer_class')(reporte_config)

    def get_object(self):
        try:
            condicao = {}
            condicao['id_dispositivo__uid'] = self.kwargs["uid"]
            condicao['id'] = self.kwargs['id']
            return Reporte.objects.get(**condicao)
        except Reporte.DoesNotExist:
            raise Reporte.NotFound(detail="Registro não encontrado", code=404)