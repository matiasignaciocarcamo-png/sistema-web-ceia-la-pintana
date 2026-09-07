# Sistema Web de Gestión Interna CEIA La Pintana — EPE 2

Proyecto de **Desarrollo Full Stack (A+S/VcM) — IPCHILE**. Esta versión corresponde a la **EPE 2** y continúa el trabajo desarrollado en Backend y la planificación Full Stack de la EPE 1.

## Estado de la EPE 2

La aplicación integra **Front-End React + Bootstrap**, **Back-End Django REST Framework** y **Base de Datos SQLite**. Incluye componentes reutilizables, consumo de API REST, operaciones CRUD, control de asistencia, alertas de asistencia inferior al 85%, inventario, agenda, usuarios y pruebas de funcionamiento.

## Estructura

- `epe2/frontend/`: interfaz React.
- `epe2/backend/`: API REST Django, modelos, migraciones y pruebas.
- `epe2/REGISTRO_PRUEBAS.md`: registro de pruebas, errores, correcciones y mejoras.
- `epe2/qa_static.py`: verificación estructural del proyecto.

## Ejecución local

### Back-End
```bash
cd epe2/backend
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python seed_demo.py
python manage.py runserver
```

### Front-End
```bash
cd epe2/frontend
npm install
npm run dev
```

## Pruebas
```bash
cd epe2/backend
python manage.py test

cd ../..
python epe2/qa_static.py
```

## Repositorio oficial de entrega

**https://github.com/matiasignaciocarcamo-png/sistema-web-ceia-la-pintana**

Proyecto preparado como evidencia de integración Front-End, Back-End y Base de Datos para la EPE 2.