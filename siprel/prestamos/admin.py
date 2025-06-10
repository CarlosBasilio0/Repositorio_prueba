from django.contrib import admin
from .models import Usuario, Equipo, Prestamo, Historial, Notificacion, Categoria, Ubicacion, Mantenimiento, Sancion, Reporte

# Registrar los modelos en el admin de Django
admin.site.register(Usuario)
admin.site.register(Equipo)
admin.site.register(Prestamo)
admin.site.register(Historial)
admin.site.register(Notificacion)
admin.site.register(Categoria)
admin.site.register(Ubicacion)
admin.site.register(Mantenimiento)
admin.site.register(Sancion)
admin.site.register(Reporte)