from django.db import models

# Create your models here.

# Group

class Group(models.Model):
    """
    Group Model
    """

    group_id = models.AutoField(primary_key = True)
    group_name = models.CharField(max_lengh = 50)
    group_score = modles.IntegerField(max_length= 50)
    survey = models.ForeignKey('Survey', on_delete = models)

class Member(models.Model):
    """
    Member Model // Inheritance from student
    """
    student = modles.ForeignKey('Student', on_delete = models)


