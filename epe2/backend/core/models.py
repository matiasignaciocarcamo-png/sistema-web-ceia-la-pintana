from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Perfil(models.Model):
    ROLES=[('ADMIN','Administrador'),('PROF','Profesor')]
    usuario=models.OneToOneField(User,on_delete=models.CASCADE,related_name='perfil')
    rol=models.CharField(max_length=10,choices=ROLES,default='PROF')
    def __str__(self): return f'{self.usuario.username} - {self.get_rol_display()}'

class Curso(models.Model):
    nombre=models.CharField(max_length=80,unique=True)
    jornada=models.CharField(max_length=30,blank=True)
    profesor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='cursos_asignados')
    activo=models.BooleanField(default=True)
    def __str__(self): return self.nombre

class Estudiante(models.Model):
    rut=models.CharField(max_length=12,unique=True)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    curso=models.ForeignKey(Curso,on_delete=models.PROTECT,related_name='estudiantes')
    activo=models.BooleanField(default=True)
    def __str__(self): return f'{self.nombres} {self.apellidos}'

class Asistencia(models.Model):
    ESTADOS=[('P','Presente'),('A','Ausente'),('J','Justificado'),('T','Atraso')]
    estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE,related_name='asistencias')
    fecha=models.DateField()
    estado=models.CharField(max_length=1,choices=ESTADOS,default='P')
    observacion=models.CharField(max_length=200,blank=True)
    registrado_por=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=['estudiante','fecha'],name='uniq_asistencia_estudiante_fecha')]
        ordering=['-fecha','estudiante__apellidos']

class Categoria(models.Model):
    nombre=models.CharField(max_length=80,unique=True)
    def __str__(self): return self.nombre

class Producto(models.Model):
    ESTADOS=[('OK','Disponible'),('BAJO','Stock bajo'),('MANT','Mantención'),('BAJA','Dado de baja')]
    codigo=models.CharField(max_length=30,unique=True)
    nombre=models.CharField(max_length=120)
    categoria=models.ForeignKey(Categoria,on_delete=models.PROTECT,related_name='productos')
    stock=models.PositiveIntegerField(default=0)
    stock_minimo=models.PositiveIntegerField(default=1)
    estado=models.CharField(max_length=10,choices=ESTADOS,default='OK')
    ubicacion=models.CharField(max_length=120,blank=True)
    def save(self,*args,**kwargs):
        if self.estado not in ('MANT','BAJA'):
            self.estado='BAJO' if self.stock <= self.stock_minimo else 'OK'
        super().save(*args,**kwargs)
    def __str__(self): return self.nombre

class Evento(models.Model):
    titulo=models.CharField(max_length=150)
    fecha=models.DateField()
    hora=models.TimeField(null=True,blank=True)
    categoria=models.CharField(max_length=80,blank=True)
    descripcion=models.TextField(blank=True)
    def __str__(self): return self.titulo
