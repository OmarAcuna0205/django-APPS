from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Breeds
    path('breeds/', views.BreedList.as_view(), name='breed-list'),
    path('breeds/<int:pk>/', views.BreedDetail.as_view(), name='breed-detail'),
    
    # Rutas para Dogs
    path('dogs/', views.DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name='dog-detail'),

    # --- RUTAS NUEVAS DEL EXAMEN ---
    
    # 1. Formulario HTML para crear [cite: 6]
    path('dogs/new/', views.dog_create_view, name='dog-create'),
    
    # 2. Lista HTML de perros 
    path('dogs/list/', views.dog_list_view, name='dog-list-html'),
    
    # 3. API Externa (JSON) [cite: 43]
    path('dogs/random-image/', views.dog_random_image_api, name='dog-random-api'),
    
    # 4. API Externa (Vista HTML) [cite: 46]
    path('dogs/random/', views.dog_random_view, name='dog-random-html'),
]