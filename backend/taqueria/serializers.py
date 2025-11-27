from rest_framework import serializers
from .models import Taco, Categoria

class TacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taco
        fields = '__all__'