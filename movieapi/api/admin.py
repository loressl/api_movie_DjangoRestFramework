from django.contrib import admin
from .models import category, movie, actor
# Register your models here.

admin.site.register(movie)
admin.site.register(actor)
admin.site.register(category)