# Proyecto Final: Taquería El Docker

Aplicación web de gestión de pedidos para una taquería, desarrollada con Django, PostgreSQL y Docker. Permite a los usuarios ver el menú, armar un carrito de compras y dar seguimiento al estado de sus pedidos.

## Características del Proyecto

### Modelos de Datos
* **Categoria & Taco:** Gestión del menú con imágenes.
* **Pedido & DetallePedido:** Relaciona usuarios con productos, calculando subtotales y totales.
* **Usuario:** Sistema nativo de Django.

### Funcionalidades Clave
1.  **Carrito de Compras:** Persistencia basada en sesiones (sin necesidad de login inicial).
2.  **Gestión de Pedidos:** Flujo completo desde la selección hasta la confirmación.
3.  **Toque Personal (Extra):** Sistema de **Estados del Pedido**. Los pedidos cambian visualmente de "Pendiente" a "En Preparación" y "Entregado".
4.  **API REST:** Endpoint `/api/tacos/` para consumo externo de datos.

### Tecnologías
* **Backend:** Django 5 + Django REST Framework.
* **Base de Datos:** PostgreSQL 16.
* **Contenedores:** Docker Compose para orquestar DB, Admin y Web.
* **Frontend:** Bootstrap 5 + JavaScript para modo oscuro y alertas.

## Cómo ejecutar

1.  Construir los contenedores:
    ```bash
    docker-compose build
    ```
2.  Iniciar el servidor:
    ```bash
    docker-compose up
    ```
3.  Acceder a la web: http://localhost:8000