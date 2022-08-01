from django.db import models

# Create your models here.

class TwoToken(models.Model):
    user_id = models.IntegerField()
    code = models.CharField(max_length=7, null=True, blank = True)
    phone = models.CharField(null=True , max_length=20)

class TwoVerify(models.Model):
    user_id = models.IntegerField()

class contact(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    query=models.TextField()

class bussiness(models.Model):
    CHOICES = (
        ('RESTURANT', 'Resturant'),
        ('PLUMBER', 'Plumber'),
        ('HOMESERVICE', 'Home Service'),
    )
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    rating = models.IntegerField()
    location = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='pics')
    category = models.CharField(
        max_length=15,
        choices=CHOICES
        )
