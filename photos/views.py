from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm , PostForm , CommentForm
from .models import Comments, Profile, Image, Like , Follow
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView    


# # # creating he login view 
# # class AdminLogin(LoginView):
# #     template_name = 'registration/login.html'

# from registration.backends.simple.views import RegistrationView

# class MyRegistrationView(RegistrationView):
#     template_name = 'registration/registration_form.html'

# Create your views here
@login_required(login_url='/accounts/login/')
def home(request):
  current_user = request.user
  timeline_items = Image.objects.all().order_by('pub_date').reverse()
  all_users = User.objects.exclude(id= request.user.id)
  # liked_posts = [i for i in Image.objects.all() if Rate.objects.filter(user = request.user, post=1)]
  # followed = [i for i in User.objects.all() if Follow.objects.filter(follower = request.user, followed=i)]
  if request.method == 'POST':
    form = PostForm(request.POST , request.FILES)
  
    if form.is_valid():
    
      poster = form.save(commit = False)
      poster.profile =  Profile.objects.get( profile_user_id = current_user.id)
      poster.save()
    return redirect('home')

  else:
    form = PostForm()

  
  context = {'post_form': form, 'images':timeline_items,  'all_users':all_users}

  return render (request, 'photos/home.html',context)

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


def comments(request):
  current_user = request.user

  
  if request.method == 'POST':
    form = CommentForm(request.POST , request.FILES)

  
    if form.is_valid():
    
      comments = form.save(commit = False)
      comments = Comments.objects.get(image_id = current_user.id)
      comments.save()
    return redirect('comments')

  else:
    form = ProfileForm()
    return render (request ,'photos/home.html',{"form":form})



# def profile_images(request,id):
#   images = Image.objects.filter(profile_id = id).all()
#   return render(request , 'photos/profile-images.html',{"images":images})


# @login_required(login_url ='/accounts/login/')
# def poster(request):
#   current_user = request.user
  
#   return render (request ,'photos/post.html',{"form":form})

