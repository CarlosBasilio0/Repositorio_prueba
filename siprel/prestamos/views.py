from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from .forms import SolicitudPublicaForm  # nuevo import

# Vista pública
def inicio(request):
    return render(request, 'inicio.html')

def solicitud_publica(request):
    if request.method == 'POST':
        form = SolicitudPublicaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'solicitud_exitosa.html')  # plantilla que haremos en el paso 5
    else:
        form = SolicitudPublicaForm()

    return render(request, 'solicitud_publica.html', {'form': form})


# Vistas del API REST
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MaestraViewSet(viewsets.ModelViewSet):
    queryset = Maestra.objects.all()
    serializer_class = MaestraSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer

class TipoEquipoViewSet(viewsets.ModelViewSet):
    queryset = TipoEquipo.objects.all()
    serializer_class = TipoEquipoSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class SolicitudPrestamoViewSet(viewsets.ModelViewSet):
    queryset = SolicitudPrestamo.objects.all()
    serializer_class = SolicitudPrestamoSerializer

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class EvaluacionPrestamoViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionPrestamo.objects.all()
    serializer_class = EvaluacionPrestamoSerializer

class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer

class IncidenteViewSet(viewsets.ModelViewSet):
    queryset = Incidente.objects.all()
    serializer_class = IncidenteSerializer

class EstadoEquipoViewSet(viewsets.ModelViewSet):
    queryset = EstadoEquipo.objects.all()
    serializer_class = EstadoEquipoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer

class AuditoriaViewSet(viewsets.ModelViewSet):
    queryset = Auditoria.objects.all()
    serializer_class = AuditoriaSerializer

class SoporteViewSet(viewsets.ModelViewSet):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer