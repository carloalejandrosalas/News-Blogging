from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm,ContactoForm
from .models import Registrado,ContactoRegistrado

# Create your views here.
def inicio(request):
	titulo = "HOLA"
	usuario = request.user

	if request.user.is_authenticated():
		titulo = "Bienvenido %s" %(usuario)
	form = RegModelForm(request.POST or None)
	#print (dir(form)) -> nos permite ver todo lo que podemos hacer con formularios

	context = {
		"titulo":titulo,
		"el_form": form,
	}

	if form.is_valid():
		instance  = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")

		if not instance.nombre:
			instance.nombre = "Persona"
		instance.save()

		context = {
			"titulo" : "Gracias %s!" %(nombre)
		}

		#form_data = form.cleaned_data
		#email = form_data.get('email')
		#nombre = form_data.get('nombre')
		#objeto = Registrado.objects.create(email=email,nombre=nombre)

	return render(request,"inicio.html",context)

def contact(request):
	form = ContactoForm(request.POST or None)
	usuario = request.user

	context = {
		"titulo":"Conctactanos",
		"usuario":usuario,
		"form":form,
	}

	if form.is_valid():
		instance  = form.save(commit=False)
		form_nombre = form.cleaned_data.get("nombre")
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")

		if not instance.nombre:
			instance.form_nombre = "Persona"
		instance.save()

		context = {
			"titulo":"Gracias por su mensaje %s!" %(form_nombre)
		}

		asunto="Form de contacto"
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre,form_mensaje,form_email)
		send_mail(
		    asunto,
		    email_mensaje,
		    email_from,
		    email_to,
		    fail_silently=False,
		)

		# for key in form.cleaned_data:
		# 	print key+":"
		# 	print form.cleaned_data.get(key)+"\n----------"
		# email =  form.cleaned_data.get('email')
		# mensaje = form.cleaned_data.get('mensaje')
		# nombre = form.cleaned_data.get('nombre')
		#print email,mensaje,nombre

	return render(request,"forms.html",context)
