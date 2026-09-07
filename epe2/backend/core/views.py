from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.utils import timezone
from .models import Curso, Estudiante, Asistencia, Categoria, Producto, Evento
from .serializers import UserSerializer, CursoSerializer, EstudianteSerializer, AsistenciaSerializer, CategoriaSerializer, ProductoSerializer, EventoSerializer
from .permissions import IsAdminOrReadOnly, AsistenciaPermission, rol_usuario

class CursoViewSet(viewsets.ModelViewSet):
    queryset=Curso.objects.select_related('profesor').all(); serializer_class=CursoSerializer; permission_classes=[IsAdminOrReadOnly]
class EstudianteViewSet(viewsets.ModelViewSet):
    serializer_class=EstudianteSerializer; permission_classes=[IsAdminOrReadOnly]
    def get_queryset(self):
        qs=Estudiante.objects.select_related('curso').prefetch_related('asistencias').all()
        curso=self.request.query_params.get('curso'); q=self.request.query_params.get('q')
        if curso: qs=qs.filter(curso_id=curso)
        if q: qs=qs.filter(Q(nombres__icontains=q)|Q(apellidos__icontains=q)|Q(rut__icontains=q))
        return qs
class AsistenciaViewSet(viewsets.ModelViewSet):
    serializer_class=AsistenciaSerializer; permission_classes=[AsistenciaPermission]
    def get_queryset(self):
        qs=Asistencia.objects.select_related('estudiante__curso').all()
        curso=self.request.query_params.get('curso'); fecha=self.request.query_params.get('fecha')
        if curso: qs=qs.filter(estudiante__curso_id=curso)
        if fecha: qs=qs.filter(fecha=fecha)
        return qs
    def perform_create(self,serializer): serializer.save(registrado_por=self.request.user)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all(); serializer_class=CategoriaSerializer; permission_classes=[IsAdminOrReadOnly]
class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class=ProductoSerializer; permission_classes=[IsAdminOrReadOnly]
    def get_queryset(self):
        qs=Producto.objects.select_related('categoria').all(); q=self.request.query_params.get('q')
        if q: qs=qs.filter(Q(nombre__icontains=q)|Q(codigo__icontains=q))
        return qs
class EventoViewSet(viewsets.ModelViewSet):
    queryset=Evento.objects.all().order_by('fecha','hora'); serializer_class=EventoSerializer; permission_classes=[IsAdminOrReadOnly]
class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all(); serializer_class=UserSerializer

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_api(request):
    username=request.data.get('username'); password=request.data.get('password')
    user=authenticate(username=username,password=password)
    if not user: return Response({'detail':'Credenciales inválidas.'},status=status.HTTP_400_BAD_REQUEST)
    token,_=Token.objects.get_or_create(user=user)
    return Response({'token':token.key,'usuario':UserSerializer(user).data})

@api_view(['GET'])
def dashboard(request):
    estudiantes=Estudiante.objects.filter(activo=True)
    total_est=estudiantes.count(); total_cursos=Curso.objects.filter(activo=True).count()
    productos_bajo=Producto.objects.filter(estado='BAJO').count()
    eventos=Evento.objects.filter(fecha__gte=timezone.localdate()).order_by('fecha')[:5]
    alertas=[]
    for e in estudiantes.prefetch_related('asistencias'):
        total=e.asistencias.count(); presentes=e.asistencias.filter(estado__in=['P','T']).count()
        porcentaje=100 if total==0 else round(presentes*100/total,1)
        if porcentaje < 85: alertas.append({'id':e.id,'nombre':str(e),'curso':e.curso.nombre,'porcentaje':porcentaje})
    return Response({'total_estudiantes':total_est,'total_cursos':total_cursos,'productos_stock_bajo':productos_bajo,'alertas_asistencia':alertas,'eventos_proximos':EventoSerializer(eventos,many=True).data})
