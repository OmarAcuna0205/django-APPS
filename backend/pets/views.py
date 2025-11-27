# pets/views.py
from django.shortcuts import render, redirect # <-- Asegúrate de importar esto
from rest_framework import generics
from rest_framework.response import Response # <-- Para la API custom
from rest_framework.decorators import api_view # <-- Para la API custom
from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer
from .forms import DogForm # <-- Importamos el form nuevo
import requests # <-- Para consumir la API externa

# --- Vistas para Breed ---

class BreedList(generics.ListCreateAPIView):
    """
    GET: Devuelve una lista de todas las razas.
    POST: Crea una nueva raza.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Devuelve los detalles de una raza específica por ID.
    PUT: Actualiza una raza específica.
    DELETE: Elimina una raza específica.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

# --- Vistas para Dog ---

class DogList(generics.ListCreateAPIView):
    """
    GET: Devuelve una lista de todos los perros.
    POST: Crea un nuevo perro.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Devuelve los detalles de un perro específico por ID.
    PUT: Actualiza un perro específico.
    DELETE: Elimina un perro específico.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

# 1. Vista del Formulario (HTML) 
def dog_create_view(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dog-list-html') # Redirige a la lista después de guardar
    else:
        form = DogForm()
    
    return render(request, 'pets/dog_form.html', {'form': form})

# 2. Vista de Lista de Perros (HTML con links a Google) [cite: 22-31]
def dog_list_view(request):
    dogs = Dog.objects.all()
    return render(request, 'pets/dog_list.html', {'dogs': dogs})

# 3. Endpoint API que consume API Externa (JSON) [cite: 43-45]
@api_view(['GET'])
def dog_random_image_api(request):
    # Consumimos la API de RandomDog
    response = requests.get('https://random.dog/woof.json')
    data = response.json()
    # Regresamos el JSON tal cual o filtrado
    return Response({
        'source': 'RandomDog API',
        'image_url': data.get('url')
    })

# 4. Vista Web que consume API Externa (HTML) [cite: 46-48]
def dog_random_view(request):
    response = requests.get('https://random.dog/woof.json')
    data = response.json()
    image_url = data.get('url')
    
    return render(request, 'pets/dog_random.html', {'image_url': image_url})