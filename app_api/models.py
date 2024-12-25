from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class User(AbstractUser):
    points = models.IntegerField(default=0)
    tasks_completed = models.IntegerField(default=0)

class AndroidApp(models.Model):
    name = models.CharField(max_length=255)
    points = models.IntegerField()

class Screenshot(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    app = models.ForeignKey(AndroidApp, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="screenshots/bg1.jpg")
