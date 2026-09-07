# Sistema Web de Gestión Interna CEIA La Pintana - EPE 2 Full Stack

Proyecto académico para la asignatura **(A+S/VcM) Desarrollo Full Stack - 2620 (B3)** de IPCHILE. Continúa el trabajo realizado en Desarrollo Backend y EPE 1 Full Stack.

## Objetivo
Integrar una interfaz React responsiva con una API REST en Django REST Framework y persistencia SQLite, priorizando gestión de estudiantes, cursos, asistencia, inventario, agenda y usuarios.

## Tecnologías
- Front-End: React, React Router, Axios, Bootstrap y CSS responsivo.
- Back-End: Python, Django, Django REST Framework y Token Authentication.
- Base de datos: SQLite en desarrollo.
- Integración: API REST JSON.

## Funcionalidades implementadas
1. Inicio de sesión y almacenamiento de token.
2. Panel principal con indicadores, eventos, stock crítico y alertas de asistencia bajo 85%.
3. Consulta y búsqueda de estudiantes.
4. Registro de asistencia por curso y fecha con validación de fecha futura y restricción de duplicidad.
5. Consulta de inventario y estado automático de stock bajo.
6. Agenda digital.
7. Consulta de usuarios y rol.
8. Permisos diferenciados: Administrador y Profesor.
9. Diseño responsivo y componentes reutilizables.

## Endpoints principales
- POST `/api/auth/login/`
- GET `/api/dashboard/`
- CRUD `/api/cursos/`
- CRUD `/api/estudiantes/`
- CRUD `/api/asistencias/`
- CRUD `/api/productos/`
- CRUD `/api/eventos/`
- GET `/api/usuarios/`

## Instalación local
### 1. Backend
```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python seed_demo.py
python manage.py runserver
```

### 2. Frontend
En otra terminal:
```bash
cd frontend
npm install
npm run dev
```
Abrir `http://localhost:5173`.

## Usuarios demo locales
- Administrador: `admin` / `Admin123!`
- Profesor: `profesor` / `Profesor123!`

> Estas credenciales son exclusivamente de demostración local y deben cambiarse antes de cualquier despliegue real.

## Pruebas automáticas del backend
```bash
cd backend
python manage.py test
```
Los tests incluidos verifican listado de estudiantes, registro de asistencia, prevención de duplicidad y estado de stock bajo.

## Estructura
```text
backend/
  ceia/              configuración Django
  core/              modelos, serializers, vistas, permisos, API y tests
  seed_demo.py       carga de datos de demostración
frontend/
  src/components/    componentes reutilizables
  src/pages/         vistas de los módulos
  src/services/      cliente Axios y autenticación
  src/styles.css     diseño responsivo
```

## Repositorio GitHub
https://github.com/matiasignaciocarcamo-png/sistema-web-ceia-la-pintana
