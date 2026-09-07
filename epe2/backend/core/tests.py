from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Perfil,Curso,Estudiante,Asistencia,Categoria,Producto
from datetime import date

class IntegracionAPITests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user('admin',password='Admin123!',is_superuser=True)
        self.client=APIClient(); self.client.credentials(HTTP_AUTHORIZATION='Token '+Token.objects.create(user=self.user).key)
        self.curso=Curso.objects.create(nombre='1° Nivel A')
        self.est=Estudiante.objects.create(rut='11.111.111-1',nombres='Ana',apellidos='Pérez',curso=self.curso)
    def test_listar_estudiantes(self):
        r=self.client.get('/api/estudiantes/'); self.assertEqual(r.status_code,200)
    def test_registrar_asistencia(self):
        r=self.client.post('/api/asistencias/',{'estudiante':self.est.id,'fecha':date.today(),'estado':'P'},format='json'); self.assertEqual(r.status_code,201)
    def test_no_duplica_asistencia(self):
        Asistencia.objects.create(estudiante=self.est,fecha=date.today(),estado='P')
        r=self.client.post('/api/asistencias/',{'estudiante':self.est.id,'fecha':date.today(),'estado':'A'},format='json'); self.assertEqual(r.status_code,400)
    def test_alerta_stock(self):
        cat=Categoria.objects.create(nombre='Computación'); p=Producto.objects.create(codigo='PC-01',nombre='Notebook',categoria=cat,stock=1,stock_minimo=2); self.assertEqual(p.estado,'BAJO')
