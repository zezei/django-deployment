from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    #Extendemos la clase de User admin
    user = models.OneToOneField(User,on_delete=models.PROTECT)

    #atributos adicionales
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics' ,blank=True)

    def __str__(self):
        return self.user.username
