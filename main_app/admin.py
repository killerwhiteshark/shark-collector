from django.contrib import admin
from .models import Shark, Feeding, Toy
# Register your models here.

admin.site.register(Shark)
admin.site.register(Feeding)
admin.site.register(Toy)