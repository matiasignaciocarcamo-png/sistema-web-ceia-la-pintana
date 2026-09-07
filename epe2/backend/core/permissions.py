from rest_framework.permissions import BasePermission, SAFE_METHODS

def rol_usuario(user):
    if user.is_superuser: return 'ADMIN'
    return getattr(getattr(user,'perfil',None),'rol','PROF')

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self,request,view):
        return request.method in SAFE_METHODS or rol_usuario(request.user)=='ADMIN'

class AsistenciaPermission(BasePermission):
    def has_permission(self,request,view):
        if request.method in SAFE_METHODS or request.method=='POST': return True
        return rol_usuario(request.user)=='ADMIN'
