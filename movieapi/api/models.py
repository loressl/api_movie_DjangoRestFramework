from django.db import models

# Create your models here.
class actor(models.Model):
   name = models.CharField(max_length = 100)
 
   class Meta:
       verbose_name_plural = "Actors"
 
   def __str__(self):
      return self.name
 
class category(models.Model):
    name = models.CharField(max_length = 100)
 
    class Meta:
        verbose_name_plural = "Categories"
 
    def __str__(self):
        return self.name
 
class movie(models.Model):
    title = models.CharField(max_length = 300)
    actors = models.ManyToManyField(actor)
    categories = models.ManyToManyField(category)
 
    class Meta:
        verbose_name_plural = "Movies"
 
    def __str__(self):
        return self.title