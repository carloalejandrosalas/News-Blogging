from django.contrib import admin

# Register your models here.
from .forms import RegModelForm,ContactoForm
from .models import Registrado,ContactoRegistrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ['email','nombre','timestamp']

	form = RegModelForm

	#list_display_links = ['email']
	list_filter = ['timestamp']
	list_editable = ['nombre']
	search_fields = ['email','nombre']
	#class Meta:
	#	model = Registrado


class AdminContactoRegistrado(admin.ModelAdmin):
	list_display = ['email','nombre','mensaje','timestamp']

	form = ContactoForm

	#list_display_links = ['email']
	list_filter = ['timestamp']
	list_editable = ['nombre']
	search_fields = ['email','nombre']
	#class Meta:
	#	model = Registrado


admin.site.register(Registrado,AdminRegistrado)
admin.site.register(ContactoRegistrado,AdminContactoRegistrado)
