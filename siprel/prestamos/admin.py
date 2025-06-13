from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Maestra,
    PerfilUsuario,
    Categoria,
    Laboratorio,
    Equipo,
    SolicitudPrestamo,
    Prestamo,
    Mantenimiento,
    Incidente,
    Notificacion,
    Auditoria,
    Archivo,
    TipoEquipo,
    EstadoEquipo,
    Reserva,
    EvaluacionPrestamo,
    Soporte
)

# Registrar los demás modelos normalmente
admin.site.register(Maestra)
admin.site.register(PerfilUsuario)  
admin.site.register(Categoria)
admin.site.register(Laboratorio)
admin.site.register(Equipo)
admin.site.register(SolicitudPrestamo)
admin.site.register(Prestamo)
admin.site.register(Mantenimiento)
admin.site.register(Incidente)
admin.site.register(Notificacion)
admin.site.register(Auditoria)
admin.site.register(Archivo)
admin.site.register(TipoEquipo)
admin.site.register(EstadoEquipo)
admin.site.register(Reserva)
admin.site.register(EvaluacionPrestamo)
admin.site.register(Soporte)