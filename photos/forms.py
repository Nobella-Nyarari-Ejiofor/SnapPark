from .models import Comments, Profile, Image
from django import forms

class ProfileForm(forms.ModelForm):
  class Meta:
     model = Profile
     exclude = ['profile_user']

class PostForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ['pub_date', 'profile']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comments
    exclude = ['image_id']