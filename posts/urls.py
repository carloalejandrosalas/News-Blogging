from django.urls import path

from . import views

app_name= 'posts'
urlpatterns = [
    path('',  views.index, name="index" ),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/edit', views.edit, name="edit")
]
