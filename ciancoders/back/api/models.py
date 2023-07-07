from django.db import models

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=100)
    imagen_empleado = models.ImageField(upload_to='empleados/', blank=True, null=True)
    salario_base_empleado = models.DecimalField(max_digits=8, decimal_places=2)
    horas_trabajadas_empleado = models.PositiveIntegerField()
    otro_campo_empleado = models.CharField(max_length=100)
    cargo_empleado = models.CharField(max_length=100)
    departamento_empleado = models.CharField(max_length=100)
    fecha_contratacion_empleado = models.DateField()
    email_empleado = models.EmailField()
    telefono_empleado = models.CharField(max_length=20)
    direccion_empleado = models.CharField(max_length=200)
    fecha_nacimiento_empleado = models.DateField()
    estado_civil_empleado = models.CharField(max_length=50)