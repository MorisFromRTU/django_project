from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class BlogPost(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
# class User(models.Model):
#     name = models.CharField(max_length = 20)
#     surname = models.CharField(max_length = 25)
#     login = models.CharField(max_length = 20, unique = True)

#     class Meta:
#         abstract = True

class Group(models.Model):
    number = models.IntegerField(unique = True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

