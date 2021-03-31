from django.db import models

# Create your models here.


class Palindrome(models.Model):
    palindrome = models.CharField(max_length=200)
