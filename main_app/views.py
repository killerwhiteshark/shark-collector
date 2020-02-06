##########################################################
from django.shortcuts import render, redirect
from .models import Shark, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

@login_required
def sharks_index(request):
  sharks = Shark.objects.filter(user=request.user)
  return render(request, 'sharks/index.html', { 'sharks': sharks })

@login_required
def sharks_detail(request, shark_id):
  shark = Shark.objects.get(id=shark_id)
  toys_shark_doesnt_have = Toy.objects.exclude(id__in = shark.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'sharks/detail.html', { 'shark': shark,'feeding_form': feeding_form, 'toys': toys_shark_doesnt_have })

@login_required
def add_feeding(request, shark_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.shark_id = shark_id
    new_feeding.save()
  return redirect('detail', shark_id=shark_id)

class SharkCreate(LoginRequiredMixin, CreateView):
  model = Shark
  fields = ['name', 'species', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class SharkUpdate(LoginRequiredMixin, UpdateView):
  model = Shark
  # Let's disallow the renaming of a Shark by excluding the name field!
  fields = ['species', 'description']

class SharkDelete(LoginRequiredMixin, DeleteView):
  model = Shark
  success_url = '/sharks/'

@login_required
def assoc_toy(request, shark_id, toy_id):
  Shark.objects.get(id=shark_id).toys.add(toy_id)
  return redirect('detail', shark_id=shark_id)

@login_required
def unassoc_toy(request, shark_id, toy_id):
  Shark.objects.get(id=shark_id).toys.remove(toy_id)
  return redirect('detail', shark_id=shark_id)

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
##########################################################