# Gestión de Taller - Django - Arquitectura del Software

## Descripción
Este proyecto consiste en el desarrollo incremental de una aplicación web en Django para la gestión de un taller de coches.

La aplicación permite registrar clientes, los coches asociados a cada cliente y los servicios realizados a esos vehículos. A lo largo de distintas prácticas se han ido incorporando nuevas funcionalidades, incluyendo configuración inicial del proyecto, enrutamiento, modelado de base de datos, vistas JSON, plantillas HTML y formularios basados en modelos.

## Objetivo del proyecto
El objetivo principal es construir una aplicación web funcional en Django aplicando progresivamente conceptos fundamentales de desarrollo backend, persistencia de datos, renderizado de vistas y organización del proyecto con control de versiones en GitHub.

## Funcionalidades implementadas

### Práctica 1 — Configuración inicial del proyecto
- Creación del entorno virtual
- Instalación de Django
- Creación del proyecto Django
- Creación de la aplicación `app_gestion_taller`
- Configuración inicial de rutas y vistas
- Integración con Git y GitHub

### Práctica 2 — URLs con parámetros y validaciones
- Uso de parámetros dinámicos en URLs
- Captura de datos mediante parámetros en las rutas
- Validación de datos recibidos
- Restricción de vistas por método HTTP

### Práctica 3 — Modelado de la base de datos
- Creación de los modelos:
  - `Cliente`
  - `Coche`
  - `Servicio`
  - `CocheServicio`
- Relaciones entre tablas:
  - Un cliente puede tener varios coches
  - Un coche puede tener varios servicios
- Migraciones de base de datos
- Registro de modelos en Django Admin

### Práctica 4 — Endpoints para registrar y consultar datos
- Registro de clientes mediante `POST`
- Registro de coches mediante `POST`
- Registro de servicios mediante `POST`
- Búsqueda de cliente por ID
- Búsqueda de coche por matrícula
- Búsqueda de coches de un cliente
- Búsqueda de servicios asociados a un coche
- Actualización de cliente
- Búsqueda de coches por marca
- Búsqueda de cliente por email

### Práctica 5 — Plantillas HTML
- Sustitución de respuestas JSON por vistas renderizadas en HTML
- Plantillas implementadas:
  - Lista de clientes
  - Detalle de cliente
  - Servicios de un coche
- Uso de:
  - `render`
  - bucles `{% for %}`
  - condicionales `{% if %}`

### Práctica 6 — Formularios basados en modelos
- Creación de `forms.py`
- Formularios basados en `ModelForm`
- Formularios para:
  - Cliente
  - Coche
  - Servicio
  - CocheServicio
- Creación de vistas para insertar datos desde formularios web
- Plantilla reutilizable `formulario.html`
- Redirección tras guardar datos

## Modelos principales

### Cliente
Guarda la información de cada cliente:
- nombre
- teléfono
- email

### Coche
Guarda la información de cada vehículo:
- marca
- modelo
- matrícula
- cliente asociado

### Servicio
Guarda la información de cada servicio del taller:
- nombre
- descripción

### CocheServicio
Tabla intermedia que relaciona coches y servicios, incluyendo:
- coche
- servicio
- fecha

## Tecnologías utilizadas
- Python
- Django
- SQLite3
- HTML
- Git
- GitHub
