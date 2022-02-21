from django.db import models

# Create your models here.
from authentication.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)


class Card(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Resource(models.Model):
    TYPES = [
        ('Reading', 'Reading Resource'),
        ('Video Course', 'Video Course'),
        ('Paid Course', 'Paid Course')
    ]
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=30, choices=TYPES)
    link = models.TextField(max_length=300)
