## Integración de API Externa (Examen 3er Parcial)

Para este examen se integró la API pública **RandomDog** para obtener imágenes aleatorias de perros.

### API Seleccionada
* **Nombre:** RandomDog API
* **URL Base:** `https://random.dog/woof.json`
* **Documentación:** https://random.dog/

### Consumo de la API
El consumo se realiza usando la librería `requests` de Python dentro de las vistas de Django (por ejemplo en `pets/views.py`). El servidor actúa como cliente: realiza una petición GET a la API externa, procesa la respuesta y la expone tanto en JSON como en HTML según la vista.

### Ejemplos de Respuesta

**1. JSON Original (Desde RandomDog):**
```json
{
    "fileSizeBytes": 436750,
    "url": "https://random.dog/1084-99b60069-4255-4220-8674-619b54835c25.jpg"
}
```

**2. JSON de Nuestra API (/api/dogs/random-image/):**
```json
{
    "source": "RandomDog API",
    "image_url": "https://random.dog/1084-99b60069-4255-4220-8674-619b54835c25.jpg"
}
```