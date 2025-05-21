from django.db import models
from django.contrib.auth.models import User

class Maestra(models.Model):
    descripcion= models.CharField(max_length=256, null=True)
    valor= models.IntegerField(null=True)
    padre_fk= models.ForeignKey("self",on_delete=models.CASCADE, null=True)


# Modelo Cliente: estudiantes o docentes
class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    TIPO_USUARIO = [
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

# Modelo Equipo: lo que se presta (computadores, proyectores, batas, etc.)
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    codigo_interno = models.CharField(max_length=50, unique=True)  # Ej. EQ-00123
    estado = models.CharField(max_length=20, choices=[
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('mantenimiento', 'En mantenimiento'),
        ('dañado', 'Dañado'),
    ], default='disponible')

    def __str__(self):
        return f"{self.nombre} - {self.codigo_interno}"

# Modelo Prestamo: une clientes con equipos, registra fechas y estado
class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='prestamos')
    equipos = models.ManyToManyField(Equipo, related_name='prestamos')
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('devuelto', 'Devuelto'),
        ('retrasado', 'Retrasado'),
    ], default='pendiente')
    entregado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='prestamos_entregados')

    def __str__(self):
        return f"Préstamo #{self.id} - {self.cliente.nombre}"

# Modelo Devolucion: registra estado final del equipo al ser devuelto
class Devolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='devoluciones')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)
    estado_final = models.CharField(max_length=20, choices=[
        ('bueno', 'Bueno'),
        ('dañado', 'Dañado'),
        ('faltante', 'Faltante'),
    ])

    def __str__(self):
        return f"Devolución de {self.equipo.nombre} - {self.estado_final}"
