from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
  title = models.CharField(max_length = 255)
  body = models.TextField(blank = True)
  created = models.DateTimeField(auto_now_add = True)
  updated = models.DateTimeField(auto_now = True)
  author = models.ForeignKey(User , on_delete = models.CASCADE)