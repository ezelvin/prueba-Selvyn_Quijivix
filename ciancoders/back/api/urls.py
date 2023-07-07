from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getEmpleados),
    path('post/', views.postEmpleados),
    path('put/<int:pk>/', views.putEmpleados),
    path('delete/<int:pk>/', views.deleteEmpleados),
]
