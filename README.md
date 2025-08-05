# Gestor de Tareas

Proyecto personal para crear una app web sencilla de gestión de tareas. Construida con Flask, diseñada para desplegar con Docker y lista para integrar CI/CD.

---

## Características

- Gestión básica de tareas: añadir, editar, eliminar.
- Interfaz sencilla con Bootstrap.
- Conexión a base de datos MongoDB.
- Dockerizado para facilitar despliegues.
- Preparado para integración continua y despliegue automático.

## Instalación y uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/beatriz2c/gestor-tareas.git
   cd gestor-tareas

2. Crea un archivo .env basado en .env.example y configura tus variables de entorno.

3. Levanta la aplicación con Docker Compose:
    ```bash
    docker compose up --build

4. Accede a la app en http://localhost:5000.

## Estructura del proyecto

- app.py: Código principal de la aplicación Flask.
- templates/: Plantillas HTML.
- Dockerfile: Imagen Docker para la app.
- docker-compose.yml: Orquestación de contenedores.
- .env.example: Variables de entorno de ejemplo.
- requirements.txt: Dependencias Python.

## Próximas mejoras
- Mejoras en interfaz y accesibilidad.
- Implementación de CI/CD completa.
- Gestión de secretos.
- Despliegue en nube.