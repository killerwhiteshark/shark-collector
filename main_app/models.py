from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Shark(models.Model):
  name = models.CharField(max_length=100)
  species = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'shark_id': self.id})

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
  max_length=1,
  # add the 'choices' field option
  choices=MEALS,
  # set the default value for meal to be 'B'
  default=MEALS[0][0]
  )
  shark = models.ForeignKey(Shark, on_delete=models.CASCADE)
  def __str__(self):
  # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"