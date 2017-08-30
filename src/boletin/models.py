from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
	nombre =  models.CharField(max_length=100,blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateField(auto_now_add=True,auto_now=False)

	def __unicode__(self): #python 2
		return self.email

	def __str__(self): #python 3
		return self.email

class ContactoRegistrado(models.Model):
	nombre = models.CharField(max_length=100,blank=True,null = True)
	email = models.EmailField()
	mensaje = models.CharField(max_length=140)
	timestamp = models.DateField(auto_now_add=True,auto_now=False)

	def __unicode__(self): #python 2
		return self.email

	def __str__(self): #python 3
		return self.email
