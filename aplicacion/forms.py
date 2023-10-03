from django import forms 

#Formularios Creacion ------------------------------------------------------------------
class TareaForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	estado = forms.CharField(max_length=100)
	creado_el = forms.DateField() #Formato AAAA-MM-DD
	
class PersonaForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	apellido = forms.CharField(max_length=100)
	fecha_nacimiento = forms.DateField() #Formato AAAA-MM-DD

class GatoForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	raza = forms.CharField(max_length=100)
	edad = forms.CharField(max_length=100)     

#Formularios Busqueda ------------------------------------------------------------------
class BuscarTareasForm(forms.Form):
	criterio_nombre = forms.CharField(max_length=100)

class BuscarPersonasForm(forms.Form):
	criterio_nombre = forms.CharField(max_length=100)

class BuscarGatosForm(forms.Form):
	criterio_nombre = forms.CharField(max_length=100)
