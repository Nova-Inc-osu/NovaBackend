from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
  user         = models.OneToOneField(User, on_delete=models.CASCADE)
  name         = models.CharField(max_length=50)
  date_created = models.DateField(auto_now_add=True)

class Patient(models.Model):
  user         = models.OneToOneField(User, on_delete=models.CASCADE)
  doctor       = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  name         = models.CharField(max_length=100)
  date_created = models.DateField(auto_now_add=True)

class Conversation(models.Model):
  participant  = models.ForeignKey(Patient, on_delete=models.CASCADE)
  date_created = models.DateField(auto_now_add=True)

class Message(models.Model):
  conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
  from_patient = models.BooleanField()
  date_created = models.DateField(auto_now_add=True)
  text         = models.CharField(max_length=1000)
