import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ceia.settings'); django.setup()
from django.contrib.auth.models import User
from core.models import Perfil,Curso,Estudiante,Asistencia,Categoria,Producto,Evento
from datetime import date,timedelta,time
admin,_=User.objects.get_or_create(username='admin',defaults={'email':'admin@ceia.cl','first_name':'Administrador'})
admin.set_password('Admin123!'); admin.is_staff=True; admin.is_superuser=True; admin.save(); Perfil.objects.get_or_create(usuario=admin,defaults={'rol':'ADMIN'})
prof,_=User.objects.get_or_create(username='profesor',defaults={'email':'profesor@ceia.cl','first_name':'Daniel','last_name':'Rojas'}); prof.set_password('Profesor123!'); prof.save(); Perfil.objects.get_or_create(usuario=prof,defaults={'rol':'PROF'})
c1,_=Curso.objects.get_or_create(nombre='1° Nivel A',defaults={'jornada':'Vespertina','profesor':prof}); c2,_=Curso.objects.get_or_create(nombre='2° Nivel B',defaults={'jornada':'Vespertina'})
for rut,nom,ape,curso in [('11.111.111-1','Ana','Pérez',c1),('12.222.222-2','Luis','Soto',c1),('13.333.333-3','María','Rojas',c2),('14.444.444-4','Pedro','Muñoz',c2)]: Estudiante.objects.get_or_create(rut=rut,defaults={'nombres':nom,'apellidos':ape,'curso':curso})
for e in Estudiante.objects.all():
    for i in range(5):
        estado='A' if e.rut.startswith('12') and i<2 else 'P'
        Asistencia.objects.get_or_create(estudiante=e,fecha=date.today()-timedelta(days=i),defaults={'estado':estado,'registrado_por':prof})
cat,_=Categoria.objects.get_or_create(nombre='Computación'); Producto.objects.get_or_create(codigo='NB-001',defaults={'nombre':'Notebook HP','categoria':cat,'stock':2,'stock_minimo':3,'ubicacion':'Sala Enlaces'}); Producto.objects.get_or_create(codigo='PR-001',defaults={'nombre':'Proyector Epson','categoria':cat,'stock':5,'stock_minimo':1,'ubicacion':'UTP'})
Evento.objects.get_or_create(titulo='Consejo de profesores',fecha=date.today()+timedelta(days=2),defaults={'hora':time(18,0),'categoria':'Reunión','descripcion':'Revisión de asistencia y casos prioritarios.'})
print('Datos demo cargados. Usuario admin/Admin123! y profesor/Profesor123!')
