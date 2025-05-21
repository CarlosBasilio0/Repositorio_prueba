from django.contrib import admin
from .models import Cliente, Maestra, Equipo, Prestamo, Devolucion

# Registrar los modelos en el admin de Django
admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Prestamo)
admin.site.register(Devolucion)
admin.site.register(Maestra)