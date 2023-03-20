from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title} ---> {self.author}'
    
    
# create a model for the search form of the bride and groom
class bridegroom(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    height = models.FloatField()
    weight = models.IntegerField()
    education = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    annual_income = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    caste = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f'Name: {self.name} ---> {self.age}'