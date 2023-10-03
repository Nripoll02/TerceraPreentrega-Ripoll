from django.db import models

class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100)
    creado_el = models.DateField() #Formato AAAA-MM-DD

    def terminar(self):
        self.estado = "terminado"

    def __str__(self):
        return f"{self.id} - {self.nombre}"


class Persona(models.Model):
	nombre = models.TextField(max_length=100)
	apellido = models.TextField(max_length=100)
	fecha_nacimiento = models.DateField() #Formato AAAA-MM-DD

	def __str__(self):
		return f"{self.id} - {self.nombre} - {self.apellido}"


class Gato(models.Model):
    nombre = models.TextField(max_length=100)
    raza = models.TextField(max_length=100)
    edad = models.TextField(max_length=100)

    def __str__(self):
	    return f"{self.id} - {self.nombre} - {self.raza}"