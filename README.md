# Sistema de Reservas de Servicios

Aplicación web desarrollada con Django para la gestión de reservas de servicios para eventos. El sistema permite administrar servicios, clientes y empleados, registrar reservas y consultar diferentes listados de información.

Además, cuenta con una API REST que permite consultar información de los servicios y clientes, así como un endpoint destinado a la visualización de reservas en un calendario. La API dispone también de documentación interactiva mediante Swagger.

---

## 📋 Descripción del proyecto

El **Sistema de Reservas de Servicios** surge a partir de la necesidad de desarrollar una aplicación base para la gestión de los servicios que una empresa ofrece para eventos.

La aplicación permite:

* Registrar y administrar clientes.
* Registrar y administrar empleados.
* Registrar y administrar coordinadores.
* Registrar y administrar los servicios ofrecidos.
* Registrar reservas de servicios para clientes.
* Consultar listados de información.
* Gestionar registros activos e inactivos mediante baja lógica.
* Consultar los servicios disponibles mediante una API REST.
* Consultar el detalle de un servicio mediante su identificador.
* Consultar información de clientes mediante la API.
* Consultar las reservas mediante un endpoint destinado a la visualización en calendario.
* Acceder a la documentación interactiva de la API mediante Swagger.

---

## 🛠️ Tecnologías utilizadas

| Tecnología                       | Uso                                                     |
| -------------------------------- | ------------------------------------------------------- |
| **Python 3.14.6**                | Lenguaje de programación                                |
| **Django 6.1**                   | Framework principal para el desarrollo web              |
| **Django REST Framework 3.18.0** | Desarrollo de la API REST                               |
| **Bootstrap**                    | Diseño y estilos de la interfaz                         |
| **Tabler**                       | Plantilla y componentes visuales de la interfaz         |
| **HTML**                         | Estructura de las páginas                               |
| **CSS**                          | Personalización de estilos                              |
| **JavaScript**                   | Interactividad del frontend                             |
| **SQLite**                       | Base de datos                                           |
| **drf-spectacular**              | Generación y documentación de la API                    |
| **Swagger UI**                   | Visualización interactiva de la documentación de la API |

---

## 📌 Requisitos previos

Antes de instalar el proyecto se necesita tener instalado:

* **Python 3.14.6**
* **Git**
* **pip**

Se recomienda utilizar Python 3.14.6 para mantener compatibilidad con las versiones utilizadas durante el desarrollo.

Para verificar la versión de Python:

```bash
python --version
```

Para verificar que Git está instalado:

```bash
git --version
```

---

## 📥 Instalación y configuración

### 1. Clonar el repositorio

Clonar el repositorio desde GitHub:

```bash
git clone https://github.com/TatoNoir/caso-negocio-aceleracion-alkemy-grupo-3
```

Ingresar al directorio del proyecto:

```bash
cd WebApp/WebApp
```


### 2. Crear el entorno virtual

Crear un entorno virtual utilizando Python:

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

#### Windows

Si se utiliza **CMD**:

```bash
.venv\Scripts\activate
```

Si se utiliza **PowerShell**:

```powershell
.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

Una vez activado el entorno virtual, debería aparecer `(.venv)` al comienzo de la línea de comandos.

### 4. Instalar las dependencias

Con el entorno virtual activado, instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

Las principales dependencias utilizadas son:

```text
Django==6.1
djangorestframework==3.18.0
drf-spectacular==0.30.0
```

---

## 🗄️ Base de datos

El proyecto utiliza **SQLite** como sistema de gestión de base de datos.

Luego de instalar las dependencias, ejecutar las migraciones:

```bash
python manage.py migrate
```

Este comando crea y actualiza las tablas necesarias para el funcionamiento de la aplicación.

---

## 👤 Superusuario

Para acceder al panel de administración de Django es necesario crear un superusuario.

Para crear un superusuario de prueba en Django, ejecutar el siguiente comando desde la carpeta del proyecto:
```
     python manage.py createsuperuser
```
Completar los datos solicitados (puede usar los de ejemplo):
```
    Username: admin
    Email address: admin@gmail.com
    Password: admin
    Password (again): admin
```
Cuando Django solicite confirmación para utilizar una contraseña débil, seleccionar **"y"**:
```
    The password is too similar to the username.
    This password is too short. It must contain at least 8 characters.
    Bypass password validation and create user anyway? [y/N]: y
```
Una vez completado el proceso, el superusuario quedará creado y podrá utilizarse para acceder al panel administrativo de Django.

El panel de administración se encuentra disponible en:

```text
/admin/
```

---

## ▶️ Ejecución del servidor

Para iniciar el servidor de desarrollo local, ejecutar:

```bash
python manage.py runserver
```

Por defecto, la aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

Para detener el servidor se puede utilizar:

```text
CTRL + C
```

---

# 🗺️ Mapa de rutas

Las rutas de la aplicación se encuentran organizadas en dos módulos principales:

* **Aplicación web:** `/`
* **API REST:** `/api/`

---

## 🌐 Rutas de la aplicación web

### Inicio

| Método | URL | Descripción                              |
| ------ | --- | ---------------------------------------- |
| GET    | `/` | Página principal y dashboard de métricas |

### Clientes

| Método     | URL                      | Descripción                          |
|------------| ------------------------ | ------------------------------------ |
| GET        | `/clientes/`             | Listado de clientes activos          |
| GET y POST | `/clientes/nuevo`        | Formulario para registrar un cliente |
| GET y POST | `/clientes/<pk>/update`  | Actualización de un cliente          |
| POST       | `/clientes/<pk>/delete`  | Eliminación lógica de un cliente     |
| GET        | `/clientes/inactivos`    | Listado de clientes inactivos        |
| POST       | `/clientes/<pk>/restore` | Restauración de un cliente           |

### Servicios

| Método     | URL                          | Descripción                             |
|------------| ---------------------------- | --------------------------------------- |
| GET        | `/servicios/`                | Listado de servicios activos            |
| GET y POST | `/servicios/nuevo/`          | Formulario para registrar un servicio   |
| GET y POST | `/servicios/<pk>/detalle/`   | Consulta y actualización de un servicio |
| POST       | `/servicios/<pk>/delete/`    | Eliminación lógica de un servicio       |
| GET        | `/servicios/inactivos`       | Listado de servicios inactivos          |
| POST       | `/servicios/<pk>/restaurar/` | Restauración de un servicio             |

### Coordinadores

| Método     | URL                           | Descripción                              |
|------------| ----------------------------- | ---------------------------------------- |
| GET        | `/coordinadores/`             | Listado de coordinadores activos         |
| GET y POST | `/coordinadores/nuevo`        | Formulario para registrar un coordinador |
| GET        | `/coordinadores/inactivos`    | Listado de coordinadores inactivos       |
| GET y POST | `/coordinadores/<pk>/update`  | Actualización de un coordinador          |
| POST       | `/coordinadores/<pk>/restore` | Restauración de un coordinador           |
| POST       | `/coordinadores/<pk>/delete`  | Eliminación lógica de un coordinador     |

### Empleados

| Método     | URL                       | Descripción                           |
|------------| ------------------------- | ------------------------------------- |
| GET        | `/empleados/`             | Listado de empleados activos          |
| GET y POST | `/empleados/nuevo`        | Formulario para registrar un empleado |
| GET        | `/empleados/inactivos`    | Listado de empleados inactivos        |
| GET y POST | `/empleados/<pk>/update`  | Actualización de un empleado          |
| POST       | `/empleados/<pk>/restore` | Restauración de un empleado           |
| POST       | `/empleados/<pk>/delete`  | Eliminación lógica de un empleado     |

### Reservas

| Método     | URL                     | Descripción                           |
|------------| ----------------------- | ------------------------------------- |
| GET        | `/reservas/`            | Listado de reservas                   |
| GET y POST | `/reservas/nueva`       | Formulario para registrar una reserva |
| GET y POST | `/reservas/<pk>/update` | Actualización de una reserva          |
| POST       | `/reservas/<pk>/delete` | Eliminación de una reserva            |

> Las rutas `<pk>` representan el identificador del registro correspondiente.

---

# 🔌 API REST

La API se encuentra disponible bajo el prefijo:

```text
/api/
```

## Servicios

### Listado de servicios

```http
GET /api/servicios/
```

Permite consultar los servicios disponibles.

### Detalle de un servicio

```http
GET /api/servicios/{servicio_id}/
```

Permite consultar el detalle completo de un servicio utilizando su identificador.

Ejemplo:

```http
GET /api/servicios/1/
```

---

## Clientes

### Listado de clientes

```http
GET /api/clientes/
```

Permite consultar el listado de clientes.

### Detalle de un cliente

```http
GET /api/clientes/{cliente_id}/
```

Permite consultar el detalle de un cliente utilizando su identificador.

Ejemplo:

```http
GET /api/clientes/1/
```

---

## Reservas

### Reservas para calendario

```http
GET /api/api/reservas-calendar/
```

Permite obtener la información de las reservas utilizada para su visualización en formato de calendario.

---

# 📚 Documentación de la API

La API cuenta con documentación generada mediante **drf-spectacular** y una interfaz interactiva utilizando **Swagger UI**.

### Esquema de la API

```text
GET /api/schema/
```

Permite acceder al esquema de la API.

### Swagger UI

```text
GET /api/swagger/
```

Permite visualizar e interactuar con los endpoints de la API desde una interfaz web.

Con el servidor iniciado, se puede acceder desde:

```text
http://127.0.0.1:8000/api/swagger/
```

---

# 📁 Estructura general del proyecto

La aplicación se encuentra organizada principalmente en dos aplicaciones Django:

```text
WebApp/
│
├── api/
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── servicios/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   └── ...
│
├── WebApp/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── templates/
│   └── ...
│
├── static/
│   └── ...
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

La aplicación `servicios` contiene la funcionalidad principal de la aplicación web, mientras que `api` contiene los endpoints destinados al acceso a los datos mediante la API REST.

---

## 🚀 Puesta en marcha rápida

Una vez clonado el proyecto, los pasos principales para ejecutarlo son:

```bash
git clone https://github.com/TatoNoir/caso-negocio-aceleracion-alkemy-grupo-3
cd WebApp

python -m venv .venv
```

Activar el entorno virtual y luego:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Finalmente, acceder desde el navegador a:

```text
http://127.0.0.1:8000/
```

Para consultar la documentación de la API:

```text
http://127.0.0.1:8000/api/swagger/
```

---

## 👥 Equipo de desarrollo

Proyecto desarrollado como parte del proceso de formación y desarrollo colaborativo del **Programa de Aceleración Tech Río Negro**.