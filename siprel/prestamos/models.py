from django.contrib.auth.models import AbstractUser
from django.db import models

# Modelo de Usuario
class Usuario(AbstractUser):
    ROLES = [
        ('administrador', 'Administrador'),
        ('docente', 'Docente'),
        ('estudiante', 'Estudiante'),
    ]
    rol = models.CharField(max_length=15, choices=ROLES)
    
    def __str__(self):
        return f"{self.username} - {self.rol}"

# Modelo de Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo de Ubicación
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo de Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('prestado', 'Prestado'), ('mantenimiento', 'En Mantenimiento')])
    fecha_adquisicion = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} - {self.estado}"

# Modelo de Préstamo
class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('devuelto', 'Devuelto')])

    def __str__(self):
        return f"Prestamo: {self.equipo.nombre} a {self.usuario.username} - {self.estado}"

# Modelo de Historial de Préstamos
class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField()
    fecha_devolucion = models.DateTimeField()

    def __str__(self):
        return f"Historial: {self.equipo.nombre} - {self.usuario.username}"

# Modelo de Mantenimiento
class Mantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    realizado_por = models.CharField(max_length=100)

    def __str__(self):
        return f"Mantenimiento de {self.equipo.nombre} - {self.fecha_mantenimiento}"

# Modelo de Sanción
class Sancion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    motivo = models.TextField()
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Sanción a {self.usuario.username} - {self.motivo}"

# Modelo de Notificación
class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación a {self.usuario.username}"

# Modelo de Reporte
class Reporte(models.Model):
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return f"Reporte generado el {self.fecha_generacion}"