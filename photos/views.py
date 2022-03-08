from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm , PostForm
from .models import Profile, Image
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView    


# creating he login view 
class AdminLogin(LoginView):
    template_name = 'registration/login.html'

# Create your views here
def welcome(request):
  return render( request , 'photos/welcome.html')

def logout(request):
  return render (request , 'registration/logout.html')

@login_required(login_url='/accounts/login/')
def profile(request):
  current_user = request.user

  
  if request.method == 'POST':
    form = ProfileForm(request.POST , request.FILES)
  
    if form.is_valid():
    
      profile = form.save(commit = False)
      profile.profile_user = current_user
      profile.save()
    return redirect('profile')

  else:
    form = ProfileForm()
    return render (request ,'photos/profile.html',{"form":form})

# def profile_images(request,id):
#   images = Image.objects.filter(profile_id = id).all()
#   return render(request , 'photos/profile-images.html',{"images":images})


@login_required(login_url ='/accounts/login/')
def poster(request):
  current_user = request.user
  if request.method == 'POST':
    form = PostForm(request.POST , request.FILES)
  
    if form.is_valid():
    
      poster = form.save(commit = False)
      poster.profile =  Profile.objects.get( profile_user_id = current_user.id)
      poster.save()
    return redirect('poster')

  else:
    form = PostForm()
  return render (request ,'photos/post.html',{"form":form})

