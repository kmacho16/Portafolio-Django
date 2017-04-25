from django.shortcuts import render,redirect
from .models import empresa,aboutme,skill,servicio,comments,categorias,proyectos
from .forms import ContactoForm,MensajeForm


# Create your views here.
def Hola(request):
	miFormulario = MensajeForm(request.POST or None)
	if miFormulario.is_valid():
		for valor in miFormulario.cleaned_data:
			print (valor)
			print (miFormulario.cleaned_data.get(valor))

	return render(request,'hola.html',{'formulario':miFormulario})

def home(request):
	miEmpresa = empresa.objects.all()
	about = aboutme.objects.all()
	skills = skill.objects.all()
	servicios = servicio.objects.all()
	comentario = comments.objects.all()
	mcategorias = categorias.objects.all()
	mproyectos = proyectos.objects.all()
	miFormulario = MensajeForm(request.POST or None)
	if miFormulario.is_valid:
		miForm = miFormulario.save(commit=False)
		miForm.revisado=False
		miForm.save()
		miFormulario = MensajeForm()

	contexto = {
	'miEmpresa':miEmpresa,
	'about':about,
	'skills':skills,
	'servicios':servicios,
	'comentarios':comentario,
	'categorias':mcategorias,
	'proyectos':mproyectos,
	'formulario':miFormulario
	}
	return render(request,'index.html',contexto)