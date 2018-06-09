from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# class Aurthor(models.Model)

class Post(models.Model):

	author= models.ForeignKey(User, on_delete=models.CASCADE)
	title= models.CharField(max_length=200)
	text=models.TextField()
	image=models.ImageField(upload_to='pictures', blank=True, null=True,  default = 'pictures/moviepass.jpg')
	date_created= models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title