from rest_framework.serializers import ModelSerializer

from .models import Empleado


class EmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'