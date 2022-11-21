from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Instructor(AbstractUser):
    """
    this is the instructor model
    """
    # any additional fields
    pass

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class Student(models.Model):
    """
    this is the student model
    """
    email = models.EmailField(max_length=256)
    name = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.email
