
#ralisé le jeudi 7novembre à21:18
# Create your models here.
from django.contrib.auth.models import AbstractUser 
from django.db import models


class CustomUser(AbstractUser):
age = models.PositiveIntegerField(null=True, blank=True)