from django.db import models


# Create your models here.
class empresa(models.Model):

	nombre = models.CharField(max_length=100)
	logo = models.ImageField(upload_to="logos/",blank=True)
	banner = models.ImageField(upload_to="banners/",blank=True)
	slogan = models.CharField(max_length=500)
	saludo = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class aboutme(models.Model):
	titulo = models.CharField(max_length=100)
	foto = models.ImageField(upload_to="about_me/",blank=True)
	contenido = models.TextField()
	def __str__(self):
		return self.titulo

class skill(models.Model):
	skill = models.CharField(max_length=100)
	porcentaje = models.IntegerField()
	def __str__(self):
		return self.skill

class servicio(models.Model):
	titulo = models.CharField(max_length=100)
	icono = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=600)
	def __str__(self):
		return self.titulo

class comments(models.Model):
	comentario = models.TextField()
	autor = models.CharField(max_length=100)
	cargo = models.CharField(max_length=100)
	foto_autor = models.ImageField("comentarios/")
	def __str__(self):
		return self.autor

class categorias(models.Model):
	nombre_cat = models.CharField(max_length=100)
	descripcion = models.TextField(blank=True)
	def __str__(self):
		return self.nombre_cat

class proyectos(models.Model):
	mi_cat = models.ForeignKey(categorias,on_delete = models.CASCADE,related_name="Proy_cat")
	nombre_proy = models.CharField(max_length=100)
	descripcion_corta = models.CharField(max_length=100)
	imagen = models.ImageField()
	descripcion = models.TextField()
	web_site = models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.nombre_proy

class mensaje(models.Model):
	nombre_cli = models.CharField(max_length=200)
	email_cli = models.CharField(max_length=200)
	mensaje_cli = models.TextField()
	revisado = models.BooleanField()
	def __str__(self):
		return self.email_cli




