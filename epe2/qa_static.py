from pathlib import Path
import ast, re, sys
ROOT=Path(__file__).parent
checks=[]
def ok(name, cond):
    checks.append((name,bool(cond)))
    print(('OK   ' if cond else 'FAIL ')+name)

pyfiles=list((ROOT/'backend').rglob('*.py'))
syntax=True
for p in pyfiles:
    try: ast.parse(p.read_text(encoding='utf-8'))
    except Exception as e:
        syntax=False; print('Syntax error',p,e)
ok('Sintaxis Python del backend',syntax)
models=(ROOT/'backend/core/models.py').read_text(encoding='utf-8')
views=(ROOT/'backend/core/views.py').read_text(encoding='utf-8')
urls=(ROOT/'backend/core/urls.py').read_text(encoding='utf-8')
serial=(ROOT/'backend/core/serializers.py').read_text(encoding='utf-8')
ok('Modelos principales definidos',all(x in models for x in ['class Curso','class Estudiante','class Asistencia','class Producto','class Evento','class Perfil']))
ok('Restricción de asistencia única', 'uniq_asistencia_estudiante_fecha' in models)
ok('Validación de fecha futura', 'No se puede registrar asistencia en una fecha futura' in serial)
ok('Dashboard y alerta <85%', 'porcentaje < 85' in views and 'dashboard' in urls)
ok('API CRUD principal registrada',all(x in urls for x in ['cursos','estudiantes','asistencias','productos','eventos','usuarios']))
ok('Migración inicial incluida',(ROOT/'backend/core/migrations/0001_initial.py').exists())
front=ROOT/'frontend/src'
required=['pages/Login.jsx','pages/Dashboard.jsx','pages/Cursos.jsx','pages/Estudiantes.jsx','pages/Asistencia.jsx','pages/Inventario.jsx','pages/Agenda.jsx','pages/Usuarios.jsx','components/Layout.jsx','services/api.js']
ok('Pantallas y componentes React incluidos',all((front/x).exists() for x in required))
api=(front/'services/api.js').read_text(encoding='utf-8')
ok('Cliente API con Token Authentication','Authorization=`Token ${token}`' in api)
app=(front/'App.jsx').read_text(encoding='utf-8')
ok('Rutas privadas configuradas','Private' in app and 'Navigate to="/login"' in app)
css=(front/'styles.css').read_text(encoding='utf-8')
ok('Diseño responsivo','@media(max-width:900px)' in css and '@media(max-width:560px)' in css)
passed=sum(v for _,v in checks)
print(f'\nResultado: {passed}/{len(checks)} verificaciones estructurales aprobadas.')
sys.exit(0 if passed==len(checks) else 1)
