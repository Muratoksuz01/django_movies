from django.db import models
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
# Create your models here.
class Movie(models.Model):
    name=models.TextField()
    description=models.TextField()
    created_date=models.DateField(auto_created=True,auto_now_add=True)
    img=models.ImageField(upload_to='proje_resimleri/')
    def __str__(self):
        return self.name
class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    profil=models.ImageField(upload_to='profile/')
    garder=models.CharField(choices=GENDER_CHOICES,max_length=20)