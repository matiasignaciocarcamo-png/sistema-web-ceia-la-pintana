from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet,EstudianteViewSet,AsistenciaViewSet,CategoriaViewSet,ProductoViewSet,EventoViewSet,UsuarioViewSet,login_api,dashboard
router=DefaultRouter()
router.register('cursos',CursoViewSet); router.register('estudiantes',EstudianteViewSet,basename='estudiantes'); router.register('asistencias',AsistenciaViewSet,basename='asistencias'); router.register('categorias',CategoriaViewSet); router.register('productos',ProductoViewSet,basename='productos'); router.register('eventos',EventoViewSet); router.register('usuarios',UsuarioViewSet)
urlpatterns=[path('auth/login/',login_api),path('dashboard/',dashboard),path('',include(router.urls))]
