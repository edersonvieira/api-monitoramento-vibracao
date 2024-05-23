from django.db import models
from django.utils.translation import gettext_lazy as _

class Dispositivo(models.Model):
    uid = models.CharField(max_length=255, unique=True, verbose_name=_("Identificador Único"))
    json_field = models.JSONField(verbose_name=_("Dados JSON"))
    data_criado = models.DateTimeField(auto_now_add=True, verbose_name=_("Data de Criação"))
    data_atualizado = models.DateTimeField(auto_now=True, verbose_name=_("Data de Atualização"))

    def __str__(self):
        return self.uid

    class Meta:
        verbose_name = _("Dispositivo")
        verbose_name_plural = _("Dispositivos")

class Reporte(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, verbose_name=_("Dispositivo"))
    json_field = models.JSONField(verbose_name=_("Dados JSON"))
    data_criado = models.DateTimeField(auto_now_add=True, verbose_name=_("Data de Criação"))
    data_atualizado = models.DateTimeField(auto_now=True, verbose_name=_("Data de Atualização"))

    def __str__(self):
        return f"{self.dispositivo.uid} - {self.data_criado.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = _("Reporte")
        verbose_name_plural = _("Reportes")