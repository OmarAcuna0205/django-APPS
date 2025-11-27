# Proyecto Final: Taquería "El Docker"

Plataforma web para la gestión de pedidos de una taquería, desarrollada con Django y Docker.

## Características del Proyecto

### 1. Modelos de Datos (Base de Datos)
El proyecto utiliza **PostgreSQL** y define relaciones clave:
* **Categoria - Taco:** Relación Uno a Muchos. Un taco pertenece a una categoría.
* **Usuario - Pedido:** Relación Uno a Muchos. Un usuario genera múltiples pedidos.
* **Pedido - DetallePedido - Taco:** Relación Muchos a Muchos (con tabla intermedia) para guardar qué tacos y cuántos de cada uno lleva un pedido.

### 2. Funcionalidades
* **Menú Dinámico:** Muestra los tacos registrados en la base de datos con sus imágenes.
* **Carrito de Compras:** Implementado con sesiones de Django (persiste mientras el navegador esté abierto).
* **Gestión de Pedidos:** Los usuarios pueden confirmar su carrito y generar un pedido.
* **Historial con Estados (Toque Personal):** Los pedidos tienen un estado visual (Pendiente, En Preparación, Entregado).
* **API REST:** Endpoint `/api/tacos/` disponible para consultar el menú en formato JSON.

### 3. Tecnologías
* **Backend:** Django 5.0
* **API:** Django REST Framework
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript.
* **Contenedores:** Docker y Docker Compose (Web, DB, pgAdmin).

## ⚙️ Cómo ejecutar

1.  **Construir los contenedores:**
    ```bash
    docker-compose build
    ```
2.  **Levantar el servidor:**
    ```bash
    docker-compose up
    ```
3.  **Entrar a la aplicación:**
    Abre tu navegador en [http://localhost:8000](http://localhost:8000)

## 📂 Estructura de Archivos Principales
* `taqueria/models.py`: Definición de tablas (Taco, Pedido, etc).
* `taqueria/views.py`: Lógica del carrito, menú y creación de pedidos.
* `taqueria/urls.py`: Rutas de la aplicación web y API.
* `docker-compose.yml`: Orquestación de servicios (Postgres y Django).