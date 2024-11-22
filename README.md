
# Gestor de Stock - Sistema de Gestión de Empleados

Este es un proyecto de Django que gestiona empleados en una empresa, permitiendo la creación, edición y eliminación de registros de empleados. El sistema utiliza un modelo de usuarios con roles de "Empleado" y "Encargado" para restringir ciertas acciones. También proporciona una interfaz de usuario donde los encargados pueden gestionar empleados y los empleados pueden realizar tareas asignadas.

## Requisitos

- Python 3.x
- Django 3.x o superior
- Bootstrap 5 (utilizado para el diseño responsivo)
- Base de datos SQLite (por defecto en Django)

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tuusuario/gestor-stock.git
   cd gestor-stock
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para sistemas Unix
   venv\Scripts\activate  # Para sistemas Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones para crear la base de datos**:
   ```bash
   python manage.py migrate
   ```

5. **Crea un superusuario para acceder al panel de administración de Django**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

7. Accede a la aplicación en tu navegador a través de `http://127.0.0.1:8000/`.

## Características

### Gestión de Empleados

- **Crear empleado**: Los encargados pueden agregar nuevos empleados a través de un formulario con campos como nombre, apellido, teléfono, correo electrónico y rol (Empleado o Encargado).
- **Ver empleados**: Los encargados pueden visualizar una lista de todos los empleados registrados.
- **Editar empleado**: Los encargados pueden modificar los datos de los empleados.
- **Eliminar empleado**: Los encargados pueden eliminar empleados del sistema.

### Roles y Autenticación

- **Roles**: El sistema utiliza dos roles de usuario: `Empleado` y `Encargado`. Los permisos varían según el rol:
  - Los empleados solo pueden realizar tareas relacionadas con sus funciones.
  - Los encargados pueden gestionar empleados, inventarios y más.
- **Autenticación**: El sistema utiliza el sistema de autenticación de Django para iniciar sesión.

## Estructura del Proyecto

- `myapp/`: Contiene las vistas, modelos y formularios principales del proyecto.
  - `models.py`: Definición del modelo `Empleado` y la relación con el usuario.
  - `views.py`: Funciones para manejar las vistas de creación, edición, visualización y eliminación de empleados.
  - `forms.py`: Formulario para crear y editar empleados.
  - `urls.py`: Rutas para acceder a las vistas de gestión de empleados y otras funciones.
  - `templates/`: Plantillas HTML para las vistas.
    - `empleados_gestion.html`: Listado de empleados.
    - `empleado_form.html`: Formulario para crear y editar empleados.
  - `static/css/`: Archivos CSS personalizados.

## Archivos de Configuración

- **`settings.py`**: Configuración de Django, incluyendo las rutas de plantillas y archivos estáticos.
- **`urls.py`**: Configuración de las URL para las vistas del proyecto.
- **`base.html`**: Plantilla base que se extiende en otras vistas.

## Funciones Pendientes

- **Gestión de Inventario**: La funcionalidad de gestión de inventario aún está pendiente de implementación.
- **Gestión de Proveedores**: Se planea agregar una vista para gestionar proveedores en el futuro.

## Contribuir

Si deseas contribuir al proyecto, puedes hacer un fork y enviar un pull request. Asegúrate de seguir las siguientes pautas:

1. Haz un fork del proyecto.
2. Crea una rama para tus cambios (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit de los mismos.
4. Envia un pull request describiendo tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.

---
