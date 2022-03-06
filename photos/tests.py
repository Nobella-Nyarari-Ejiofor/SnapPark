from django.test import TestCase
from .models import Image, User , Rate , Comments








# Create your tests here.
class ImageTestClass(TestCase):
  def setUp(self):
    self.selfie = Image(image_url = "", image_name="selfie" , image_caption = "A cute selfie for my memories",pub_date="", user = "")






