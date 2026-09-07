from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Count, Q
from .models import Perfil, Curso, Estudiante, Asistencia, Categoria, Producto, Evento

class UserSerializer(serializers.ModelSerializer):
    rol=serializers.SerializerMethodField()
    class Meta: model=User; fields=['id','username','first_name','last_name','email','rol']
    def get_rol(self,obj): return getattr(getattr(obj,'perfil',None),'rol','PROF')

class CursoSerializer(serializers.ModelSerializer):
    profesor_nombre=serializers.CharField(source='profesor.get_full_name',read_only=True)
    estudiantes_count=serializers.IntegerField(source='estudiantes.count',read_only=True)
    class Meta: model=Curso; fields='__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    curso_nombre=serializers.CharField(source='curso.nombre',read_only=True)
    porcentaje_asistencia=serializers.SerializerMethodField()
    alerta=serializers.SerializerMethodField()
    class Meta: model=Estudiante; fields='__all__'
    def get_porcentaje_asistencia(self,obj):
        total=obj.asistencias.count()
        if total==0: return 100.0
        presentes=obj.asistencias.filter(estado__in=['P','T']).count()
        return round(presentes*100/total,1)
    def get_alerta(self,obj): return self.get_porcentaje_asistencia(obj) < 85

class AsistenciaSerializer(serializers.ModelSerializer):
    estudiante_nombre=serializers.CharField(source='estudiante.__str__',read_only=True)
    curso_nombre=serializers.CharField(source='estudiante.curso.nombre',read_only=True)
    class Meta: model=Asistencia; fields='__all__'; read_only_fields=['registrado_por']
    def validate_fecha(self,fecha):
        from django.utils import timezone
        if fecha > timezone.localdate(): raise serializers.ValidationError('No se puede registrar asistencia en una fecha futura.')
        return fecha

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta: model=Categoria; fields='__all__'
class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre=serializers.CharField(source='categoria.nombre',read_only=True)
    class Meta: model=Producto; fields='__all__'
class EventoSerializer(serializers.ModelSerializer):
    class Meta: model=Evento; fields='__all__'
