from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dispositivos/', DispositivoLC.as_view()),
    path('dispositivo/<int:uid>/', DispositivoRUD.as_view()),
    path('<int:uid>/reportes/', ReporteLC.as_view()),
    path('<int:uid>/reporte/<int:id>', ReporteRUD.as_view())
]
