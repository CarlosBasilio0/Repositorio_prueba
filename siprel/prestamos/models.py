from django.db import models
from django.contrib.auth.models import User

# Modelo genérico para listas de valores (ejemplo: tipos, categorías)
class Maestra(models.Model):
    #Texto para describir el valor
    descripcion= models.CharField(max_length=256, null=True)
    #Numero entero que se puede asociar
    valor= models.IntegerField(null=True)
    #Autoreferencia para crear jerarquías simples
    padre_fk= models.ForeignKey("self",on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.descripcion #Muestra la descripción como texto
    
class Categoria(models.Model):
    #Nombre de la categoría (ejemplo: PC's, Proyectores)
    nombre = models.CharField(max_length=50)
    #Descripcion opcional de la categoría
    descripcion = models.CharField(blank=True)
    
    def __str__(self):
        return self.nombre #Muestra el nombre del admin


# Modelo Cliente: estudiantes o docentes
class Cliente(models.Model):
    identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)

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
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True) #Categoria
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


    def __str__(self):
        return f"{self.nombre} ({self.codigo_interno})" "Muestra nombre y codigo"

# Modelo Prestamo: une clientes con equipos, registra fechas y estado
class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Cliente que toma prestados
    equipos = models.ManyToManyField(Equipo) #Lista de equipos prestados
    fecha_prestamo = models.DateField(auto_now_add=True) # Fecha de creación automática
    fecha_devolucion = models.DateField()   # Fecha en la que debe devolverse
    entregado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) #Quien registró
    
    # Estado del préstamo
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('devuelto', 'Devuelto'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
   

    def __str__(self):
        return f"Préstamo #{self.id} - {self.cliente.nombre}" # Identificacion simple

# Modelo Devolucion: registra estado final del equipo al ser devuelto
class Devolucion(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE) # Préstamo al que pertenece
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE) #Equipo que se devuelve
    fecha_devolucion = models.DateField(auto_now_add=True) # Fecha real de devolución
    observaciones = models.TextField(blank=True, null=True) # Comentarios adicionales
    
    # Estado final del equipo
    ESTADO_FINAL_CHOICES = [
        ('bueno', 'Bueno'),
        ('danado', 'Dañado'),
        ('faltante', 'Faltante'),
    ]
    
    estado_final = models.CharField(max_length=20, choices=ESTADO_FINAL_CHOICES)

    def __str__(self):
        return f"Devolución de {self.id} - {self.equipo.codigo_interno}" # Texto de identificación
    
# Nuevo modelo: Notificacion para alertas y recordatorios
class Notificacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)     # Cliente destinatario de la notificación
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, null=True, blank=True)  # Préstamo relacionado (opcional)
    mensaje = models.TextField()                                      # Contenido del mensaje
    fecha_envio = models.DateTimeField(auto_now_add=True)             # Marca fecha y hora de envío
    leida = models.BooleanField(default=False)                        # Indica si el cliente vio la notificación

    def __str__(self):
        estado = 'Leída' if self.leida else 'No leída'
        return f"Notificación #{self.id} ({estado})"  # Breve descripción de la notificación
