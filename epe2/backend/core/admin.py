from django.contrib import admin
from .models import Perfil,Curso,Estudiante,Asistencia,Categoria,Producto,Evento
for model in [Perfil,Curso,Estudiante,Asistencia,Categoria,Producto,Evento]: admin.site.register(model)
