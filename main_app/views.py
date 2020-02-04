##########################################################
from django.shortcuts import render
from .models import Shark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse ### ADDED HTTPRESPONSE MODULE FOR ONLY RESPONSES
# Create your views here.

# class Shark:
#   def __init__(self, name, species, description):
#     self.name = name
#     self.species = species
#     self.description = description

# Add the following import
# Define the home view
# sharks = [
#     Shark('Bruce', 'Great White Shark', 'Sneaky boii'),
#     Shark('Sushi', 'Mako Shark', 'ALLLLLLLLLL TEEF'),
#     Shark('Bubbles', 'Black Tip Reef', 'Too nosey')
# ]
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def sharks_index(request):
  sharks = Shark.objects.all()
  return render(request, 'sharks/index.html', { 'sharks': sharks })

def sharks_detail(request, shark_id):
  shark = Shark.objects.get(id=shark_id)
  return render(request, 'sharks/detail.html', { 'shark': shark })

class SharkCreate(CreateView):
  model = Shark
  fields = '__all__'
  success_url = '/sharks/'

class SharkUpdate(UpdateView):
  model = Shark
  # Let's disallow the renaming of a Shark by excluding the name field!
  fields = ['species', 'description']

class SharkDelete(DeleteView):
  model = Shark
  success_url = '/sharks/'
##########################################################