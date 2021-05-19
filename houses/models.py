from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    type_of_business = (
        ('Rent', 'Rent'),
        ('Buy', 'Buy')


    )

    location = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    details = models.CharField(max_length=100)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    Descriptions = models.CharField(max_length=900, default='elezea kuhusu nyumba')
    image = models.ImageField(upload_to='pics',default='1.jpg')
    image1 = models.ImageField(upload_to='pics',default='1.jpg')
    image2 = models.ImageField(upload_to='pics',default='1.jpg')
    Rent_or_Buy = models.CharField(max_length=10, default='', choices=type_of_business)

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('Estate-detail', kwargs={'pk': self.pk})


