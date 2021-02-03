from django.db import models

# Create your models here.
class user(models.Model):
    email: str
    username: str
    password1 : int
    password2 : int