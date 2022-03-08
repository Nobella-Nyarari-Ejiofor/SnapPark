from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  profile_photo = models.ImageField(upload_to="profile")
  profile_bio = models.TextField(max_length= 50)
  profile_user = models.OneToOneField(User, on_delete=models.CASCADE , primary_key= True , null= False)
  
  def __str__(self):
    return self.profile_bio
 
  @classmethod
  def search_profile_by_username(cls,usersname):
    user_found = cls.objects.filter(usersname = User.objects.filter(username__contains = usersname).first()).all()
    return user_found



class Image(models.Model):
  image = models.ImageField(upload_to='images')
  image_name = models.CharField(max_length=30)
  image_caption = models.TextField(max_length = 100)
  pub_date = models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
  

  def __str__(self):
    return self.image_name

# saving image
  def save_image(self):
    self.save()

#delete image
  def delete_image(self):
    Image.objects.filter(id = self.id).delete()
 
#filter images by user
  @classmethod
  def filter_by_user(cls,user):
   images_found = cls.objects.filter(user = User.objects.filter(username_contains = user).first()).all()
   return images_found
  
class Comments(models.Model):
  comment = models.TextField()
  image = models.ForeignKey(Image , on_delete=models.CASCADE)

  def __str__(self):
    return self.comment

  # saving a comment
  def save_comment(self):
    return self.save()

  #delete a comment 
  def delete_comment(self):
    Comments.objects.filter(id = self.id).delete()

  #getting comments from one image 
  @classmethod
  def filter_by_image(cls,image):
    comments_found = cls.objects.filter(image = Image.objects.filter(id = image).first()).all()
    return comments_found


class Rate(models.Model):
  rate = models.CharField(max_length = 4)
  image= models.ForeignKey(Image , on_delete= models.CASCADE)

  def __str__(self):
    self.rate




