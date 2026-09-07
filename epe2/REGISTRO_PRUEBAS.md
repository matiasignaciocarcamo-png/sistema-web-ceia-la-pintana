# Registro de pruebas - EPE 2

| ID | Prueba | Resultado esperado | Evidencia / resultado | Estado |
|---|---|---|---|---|
| P01 | Inicio de sesión válido | Entrega token y datos de usuario | `POST /api/auth/login/`; Login guarda token y redirige | Implementado |
| P02 | Inicio de sesión inválido | Mensaje comprensible | API responde 400 y Login muestra error | Implementado |
| P03 | Consulta de estudiantes | Mostrar datos de API | `GET /api/estudiantes/` + tabla React | Implementado |
| P04 | Búsqueda de estudiantes | Filtrar nombre/apellido/RUT | parámetro `q` en ViewSet | Implementado |
| P05 | CRUD de estudiantes | Crear, editar y eliminar | formulario y acciones en `Estudiantes.jsx` | Implementado |
| P06 | Registro de asistencia | Crear un registro diario | `POST /api/asistencias/` | Implementado |
| P07 | Duplicidad de asistencia | Rechazar segundo registro estudiante/fecha | UniqueConstraint + test automático | Implementado |
| P08 | Fecha futura | Rechazar registro | `validate_fecha()` | Implementado |
| P09 | Alerta de asistencia | Destacar porcentaje inferior a 85% | serializer + dashboard | Implementado |
| P10 | Stock bajo | Estado automático si stock <= mínimo | `Producto.save()` + test | Implementado |
| P11 | CRUD inventario/agenda/cursos | Alta, edición y eliminación según permisos | formularios React + ViewSets | Implementado |
| P12 | Permisos | Profesor sin escritura administrativa | `IsAdminOrReadOnly` / `AsistenciaPermission` | Implementado |
| P13 | Responsividad | Reorganización de interfaz | media queries 900px y 560px | Implementado |
| P14 | Revisión estructural | Todos los chequeos internos aprobados | `python qa_static.py` = 11/11 | APROBADO |

## Pruebas automáticas incluidas
Ejecutar, después de instalar las dependencias:

```bash
cd backend
python manage.py test
```

Los tests cubren listado de estudiantes, registro de asistencia, prevención de duplicidad y regla de stock bajo.

## Mejoras para siguiente etapa
- Ejecutar pruebas End-to-End en navegador.
- Migrar SQLite a PostgreSQL para producción.
- Reforzar autenticación con JWT o mecanismo institucional.
- Incorporar validación formal del socio comunitario.
- Preparar despliegue y variables de entorno seguras.
