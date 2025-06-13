from django.contrib.auth.models import User
from django.db import models
from datetime import date

# 1. Maestra
class Maestra(models.Model):
    descripcion = models.CharField(max_length=256, null=True)
    valor = models.IntegerField(null=True)
    padre_fk = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descripcion or "Maestra sin descripción"

# 2. Perfil de Usuario
class PerfilUsuario(models.Model):
    ROLES = [
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('administrativo', 'Administrativo'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.rol}"

# 3. Categoría de equipos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
<<<<<<< HEAD
    descripcion = models.TextField(blank=True)
=======
    descripcion = models.TextField()
    codigo_interno = models.CharField(max_length=50, unique=True)  # Ej. EQ-00123
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True)
    marca = models.CharField(max_length=50, blank=True) #Marca del equipo
    modelo = models.CharField(max_length=50, blank=True) #Modelo del equipo
    
    # Estados posibles del equipo
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('mantenimiento', 'En mantenimiento'),
        ('danado', 'Dañado'),
    ]
    
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible') #Estado actual

>>>>>>> 424d02f (Actualización del proyecto con nuevas migraciones y modelos)

    def __str__(self):
        return self.nombre

# 4. Laboratorio
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='laboratorios')

    def __str__(self):
        return self.nombre

# 5. Tipo de equipo
class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 6. Equipo
class Equipo(models.Model):
    codigo = models.CharField(max_length=10, unique=True, default='EQ001')
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_adquisicion = models.DateField(default=date.today)
    estado = models.CharField(max_length=50, default='Disponible')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

# 7. Solicitud de préstamo
class SolicitudPrestamo(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Solicitud: {self.usuario.username} → {self.equipo.nombre}"

# 8. Archivo adjunto a la solicitud
class Archivo(models.Model):
    solicitud = models.ForeignKey(SolicitudPrestamo, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='solicitudes/')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.archivo.name

# 9. Préstamo registrado
class Prestamo(models.Model):
    solicitud = models.OneToOneField(SolicitudPrestamo, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    recibido_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='prestamos_recibidos')

    def __str__(self):
        return f"Préstamo: {self.solicitud.equipo.nombre} a {self.solicitud.usuario.username}"

# 10. Evaluación del préstamo
class EvaluacionPrestamo(models.Model):
    prestamo = models.OneToOneField(Prestamo, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Evaluación · {self.prestamo.solicitud.usuario.username}"

# 11. Mantenimiento del equipo
class Mantenimiento(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    descripcion = models.TextField()
    realizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Mantenimiento {self.fecha} · {self.equipo.nombre}"

# 12. Reporte de incidentes
class Incidente(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    resuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"Incidente · {self.equipo.nombre} · {self.usuario.username}"

# 13. Historial de estados del equipo
class EstadoEquipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.equipo.nombre} · {self.estado} · {self.fecha}"

# 14. Reserva futura del equipo
class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_reserva = models.DateField(default=date.today)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Reserva · {self.equipo.nombre} · {self.usuario.username}"

# 15. Notificación al usuario
class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación para {self.usuario.username}"

# 16. Auditoría del sistema
class Auditoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    accion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Auditoría · {self.usuario} · {self.fecha}"

# 17. Soporte al usuario
class Soporte(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    respondido = models.BooleanField(default=False)

    def __str__(self):
        return f"Soporte · {self.usuario.username}"