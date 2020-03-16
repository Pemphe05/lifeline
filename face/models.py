from django.db import models

class Cover(models.Model):
    title = models.CharField(max_length=200)
    bar = models.CharField(max_length=200)
    cantact = models.CharField(max_length=200)  

    def __str__(self):
        return self.title

class Resources(models.Model):
    categories = models.CharField(max_length= 10)
        
    def __str__(self):
        return self.categories

class AboutUs(models.Model):
    history = models.CharField(max_length=1000)
    pillars = models.CharField(max_length=1000)
    hands = models.CharField(max_length=500)
    contact = models.CharField(max_length=200)

    def __str__ (self):
        return self.pillars
