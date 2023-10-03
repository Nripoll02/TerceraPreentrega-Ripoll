from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from aplicacion.models import Tarea,Persona,Gato
from aplicacion.forms import TareaForm,PersonaForm,GatoForm
from aplicacion.forms import BuscarTareasForm, BuscarPersonasForm, BuscarGatosForm


def index (request):
	return render(request, "aplicacion/index.html")

#Mostrar ---------------------------------------------------------------------------------------------------- #Mostrar
def mostrar_tarea(request):

	tareas = Tarea.objects.all
	total_tareas = len(tareas())
	context ={
		"tareas": tareas,
		"total_tareas":total_tareas,
		"form":TareaForm(),
	}
	return render(request,"aplicacion/tareas.html", context)
#---------------------------------------------|
def mostrar_persona(request):

	personas = Persona.objects.all
	total_personas = len(personas())
	context = {
		"personas": personas,
		"total_personas":total_personas,
		"form":PersonaForm(),
	}
	return render(request,"aplicacion/personas.html", context)
#---------------------------------------------|
def mostrar_gato(request):

	gatos = Gato.objects.all
	total_gatos = len(gatos())
	context = {
		"gatos": gatos,
		"total_gatos":total_gatos,
		"form":GatoForm(),
	}
	return render(request,"aplicacion/gatos.html", context)

#Creacion ---------------------------------------------------------------------------------------------------- #Creacion
def crear_tarea(request):

	f = TareaForm(request.POST)
	context = {
		"form": f
	}

	if f.is_valid():
		Tarea(nombre=f.data["nombre"], estado=f.data["estado"], creado_el=f.data["creado_el"]).save()
		context['form'] = TareaForm()

	context["tareas"] = Tarea.objects.all()
	context["total_tareas"] = len(Tarea.objects.all())

	return render(request,"aplicacion/tareas.html", context)
#---------------------------------------------|
def crear_persona(request):

	f = PersonaForm(request.POST)
	context = {
		"form": f
	}

	if f.is_valid():
		Persona(nombre=f.data["nombre"], apellido=f.data["apellido"], fecha_nacimiento=f.data["fecha_nacimiento"]).save()
		context['form'] = PersonaForm()

	context["personas"] = Persona.objects.all()
	context["total_personas"] = len(Persona.objects.all())

	return render(request,"aplicacion/personas.html", context)
#---------------------------------------------|
def crear_gato(request):

	f = GatoForm(request.POST)
	context = {
		"form":f
	}

	if f.is_valid():
		Gato(nombre=f.data["nombre"], raza=f.data["raza"], edad=f.data["edad"]).save()
		context['form'] = GatoForm()

	context["gatos"] = Gato.objects.all()
	context["total_gatos"] = len(Gato.objects.all())

	return render(request,"aplicacion/gatos.html", context)
#Busqueda ---------------------------------------------------------------------------------------------------- #Busqueda
class BuscarTareas(ListView):
	model = Tarea
	context_object_name="tareas"

	def get_queryset(self):
		f = BuscarTareasForm(self.request.GET)
		if f.is_valid():
			return Tarea.objects.filter(nombre__icontains=f.data ["criterio_nombre"]).all()
		return Tarea.objects.none()
#---------------------------------------------|
class BuscarPersonas(ListView):
	model = Persona
	context_object_name="personas"

	def get_queryset(self):
		f = BuscarPersonasForm(self.request.GET)
		if f.is_valid():
			return Persona.objects.filter(nombre__icontains=f.data ["criterio_nombre"]).all()
		return Persona.objects.none()
#---------------------------------------------|
class BuscarGatos(ListView):
	model = Gato
	context_object_name="gatos"

	def get_queryset(self):
		f = BuscarGatosForm(self.request.GET)
		if f.is_valid():
			return Gato.objects.filter(nombre__icontains=f.data ["criterio_nombre"]).all()
		return Gato.objects.none()
