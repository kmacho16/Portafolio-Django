from django.contrib import admin
from .models import empresa,aboutme,skill,servicio,comments,categorias,proyectos,mensaje
from django.db import models
from draceditor.widgets import AdminDraceditorWidget

# Register your models here.
class AdminEmpresa(admin.ModelAdmin):
	list_display = ['id','nombre','slogan','saludo']
	list_editable = ['nombre','slogan','saludo']
	search_fields = ['slogan','nombre']
	#list_filter = ['saludo']

class AdminAboutme(admin.ModelAdmin):
	formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }

class AdminSkills(admin.ModelAdmin):
	list_display = ["skill","porcentaje"]
	list_editable = ["porcentaje"]

class AdminProyectos(admin.ModelAdmin):
	list_display=["nombre_proy","mi_cat"]
	list_filter = ["mi_cat"]

class AdminMensajes(admin.ModelAdmin):
	list_display=["email_cli","revisado"]
	list_filter = ["revisado"]


admin.site.register(empresa,AdminEmpresa)
admin.site.register(aboutme,AdminAboutme)
admin.site.register(skill,AdminSkills)
admin.site.register(servicio)
admin.site.register(comments)

admin.site.register(categorias)
admin.site.register(proyectos,AdminProyectos)
admin.site.register(mensaje,AdminMensajes)
