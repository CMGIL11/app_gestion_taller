# Gestión de Taller - Django

## Descripción

Este proyecto consiste en el desarrollo de una aplicación web con Django para la gestión básica de un taller de coches. Permite registrar clientes, los vehículos asociados a cada cliente y los servicios realizados a esos vehículos. Además, incluye una base de datos relacional, gestión desde el panel de administración de Django y vistas en formato JSON para consultar la información almacenada.

## ¿En qué consiste el proyecto?

La aplicación está pensada para organizar la información principal de un taller de coches de forma sencilla. El sistema almacena los datos de los clientes, los coches que pertenecen a cada uno y los servicios que recibe cada vehículo. Para ello, se ha diseñado una estructura de base de datos con relaciones entre las distintas entidades, permitiendo representar de forma clara la información del taller.

También se ha incluido la configuración básica de la aplicación en Django, la creación de migraciones, el registro de modelos en el panel de administración y varias rutas para consultar datos en formato JSON.

## Funcionalidades

- Registro de clientes
- Registro de coches asociados a cada cliente
- Registro de servicios realizados
- Relación entre coches y servicios
- Panel de administración con Django Admin
- Consultas de clientes en formato JSON

## Modelos principales

- **Cliente**: guarda nombre, teléfono y email
- **Coche**: guarda marca, modelo y matrícula, y se relaciona con un cliente
- **Servicio**: guarda el nombre y la descripción del servicio
- **CocheServicio**: tabla intermedia para relacionar coches y servicios junto con la fecha

## Tecnologías utilizadas

- Python
- Django
- SQLite3

## Rutas principales

- `/admin/`
- `/gestion/clientes/`
- `/gestion/clientes/<id>/`
