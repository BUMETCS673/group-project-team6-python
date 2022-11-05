from django.db import models
from django.db.models import CASCADE


# Create your models here.

# Group

class Group(models.Model):
	"""
    Group Model
    """

	group_id = models.AutoField(primary_key=True)
	group_name = models.CharField(max_length=50)
	group_score = models.IntegerField()
	instance_config = models.ForeignKey('iGroup.ConfigInstance',on_delete=CASCADE)


class Member(models.Model):
	"""
    Member Model // Inheritance from student
    """
	student = models.ForeignKey('account.Student', on_delete=CASCADE)
