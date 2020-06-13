from django.db import models

# Creat user models
class User(models.Model):
    username=models.CharField(max_length=32,primary_key=True)
    password=models.CharField(max_length=256)
    email=models.EmailField(max_length=254,unique=True, blank=False)
    mod_data=models.DateTimeField(auto_now=True)
    repair = models.BooleanField(verbose_name="是否为维修工",default=False)