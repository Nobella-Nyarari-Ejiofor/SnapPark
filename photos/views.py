from django.http import HttpResponse
from django.shortcuts import render


# Create your views here
def welcome(request):
  return render( request , 'photos/welcome.html')

def logout(request):
  return render (request , 'registration/logout.html')