from django import forms
from .models import mensaje

class ContactoForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()

class MensajeForm(forms.ModelForm):		
	class Meta:
		model = mensaje
		#fields = {"nombre_cli","email_cli","mensaje_cli"}
		exclude = {"revisado"}
		widgets={
		"nombre_cli":forms.TextInput(attrs={"placeholder":"Ingrese su nombre","class":"form-control"}),
		"email_cli":forms.TextInput(attrs={"placeholder":"Ingrese su Email","class":"form-control"}),
		"mensaje_cli":forms.Textarea(attrs={"placeholder":"Deje su comentario","class":"form-control"}),
		}
		labels={
		"nombre_cli":"",
		"email_cli":"",
		"mensaje_cli":"",
		}
	def clean_mensaje_cli(self):
		mensaje_cli = self.cleaned_data.get("mensaje_cli")
		return mensaje_cli

