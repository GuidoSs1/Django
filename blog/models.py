from django.db import models

#Cada vez que se modifique este archivo se debera migrar en consola de la siguiente forma 
# python manage.py makemigration blog(nombre de la aplicacion)
# python manage.py migrate
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=250) #Campo de caracteres, letra y numeros
    content=models.TextField()