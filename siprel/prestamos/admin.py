from django.contrib import admin
from .models import Cliente, Categoria, Maestra, Equipo, Prestamo, Devolucion

# Registrar los modelos en el admin de Django
admin.site.register(Maestra)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Equipo)
admin.site.register(Prestamo)
admin.site.register(Devolucion)