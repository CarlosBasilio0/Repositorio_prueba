from django.contrib import admin
from .models import Cliente, Prestamo, Pago

admin.site.register(Cliente)
admin.site.register(Prestamo)
admin.site.register(Pago)
