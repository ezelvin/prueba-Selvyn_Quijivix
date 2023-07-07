from rest_framework.response import Response 
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view

from .models import Empleado
from .serializers import EmpleadoSerializer


@api_view(['GET'])
def getEmpleados(request):
    empleado = Empleado.objects.all()
    serializer = EmpleadoSerializer(empleado, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postEmpleados(request):
    data = request.data
    empleado = Empleado.objects.create(
        nombre_empleado= data['nombre_empleado']
    )
    serializer = EmpleadoSerializer(empleado, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def putEmpleados(request, pk):
    data = request.data
    empleado = Empleado.objects.get(id=pk)
    serializer = EmpleadoSerializer(instance=empleado, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def deleteEmpleados(request, pk):
    empleado = Empleado.objects.get(id=pk)
    empleado.delete()
    return Response('Eliminado')
