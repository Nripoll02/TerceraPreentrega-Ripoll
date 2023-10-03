from django.contrib import admin
from django.urls import path
from aplicacion.views import index
from aplicacion.views import mostrar_tarea, mostrar_persona, mostrar_gato
from aplicacion.views import crear_tarea, crear_persona, crear_gato
from aplicacion.views import BuscarTareas, BuscarPersonas, BuscarGatos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    #Mostar URL--------------------------------------------|
    path('tareas', mostrar_tarea, name="tareas"),
    path('personas', mostrar_persona, name="personas"),
    path('gatos', mostrar_gato, name="gatos"),
    #Creacion URL------------------------------------------|
    path('tareas/create', crear_tarea, name="tareas-create"),
    path('personas/create', crear_persona, name="personas-create"),
    path('gatos/create', crear_gato, name="gatos-create"),
    #Busqueda URL------------------------------------------|
    path('tareas/list', BuscarTareas.as_view(), name="tareas-list"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    path('gatos/list', BuscarGatos.as_view(), name="gatos-list"),
]