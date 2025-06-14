from django.contrib import admin
from django.urls import path, include
from prestamos import views
from rest_framework import routers
from prestamos.views import *

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'maestra', MaestraViewSet)
router.register(r'perfiles', PerfilUsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'laboratorios', LaboratorioViewSet)
router.register(r'tipo-equipo', TipoEquipoViewSet)
router.register(r'equipos', EquipoViewSet)
router.register(r'solicitudes', SolicitudPrestamoViewSet)
router.register(r'archivos', ArchivoViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'evaluaciones', EvaluacionPrestamoViewSet)
router.register(r'mantenimientos', MantenimientoViewSet)
router.register(r'incidentes', IncidenteViewSet)
router.register(r'estados', EstadoEquipoViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'notificaciones', NotificacionViewSet)
router.register(r'auditorias', AuditoriaViewSet)
router.register(r'soporte', SoporteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # ya existente
    # 🔽 NUEVA RUTA PARA SOLICITUD PÚBLICA
    path('solicitar/', views.solicitud_publica, name='solicitud_publica'),
    path('solicitud_exitosa/', views.solicitud_exitosa, name='solicitud_exitosa'),  # ✅ NUEVA RUTA
    path('api/', include(router.urls)),      # ya existente

   
]
