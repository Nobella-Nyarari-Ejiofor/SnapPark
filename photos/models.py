from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Image(models.Model):
  image = models.ImageField(upload_to='images')
  image_name = models.CharField(max_length = 30)
  image_caption = models.TextField(max_length = 100)
  pub_date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
 

class Comments(models.Model):
  comment = models.TextField()
  image = models.ForeignKey(Image)

class Rate(models.MOdel):
  rate = models.CharField(max_length =4)
  image= models.ForeignKey(Image)






