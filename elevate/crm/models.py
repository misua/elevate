from django.db import models
# from django.views import View
from django.shortcuts import render
# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Review(models.Model):

    reviewer_name = models.CharField(max_length=50)
    review_title = models.CharField(max_length=100)

    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.reviewer_name
    

   