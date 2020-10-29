from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    field_levels =  (('l1', 'level 1'),
        ('l2', 'level 2'),('l3', 'level 3'),('l4', 'level 4'),('l5', 'level 5'),('l6', 'level 6'),
        ('l7', 'level 7'),('l8', 'level 8'),('l9', 'level 9'),('l10', 'level 10'))

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=80)
    age = models.IntegerField()
    salary = models.FloatField()
    position = models.CharField(max_length=50, choices=field_levels)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.user.username
