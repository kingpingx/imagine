from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.
CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('rather not to say', 'Rather not to say'),
    ]

class User_profile(models.Model):

    username = models.CharField(max_length=30, blank=False, default="usern")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ph_number = models.IntegerField(blank=False)
    email_id = models.EmailField(max_length=254, blank=False, default='xxx@gmail.com')
    gender = models.CharField(max_length=20, choices=CHOICES, default='select')
    address = models.CharField(max_length=200, blank=False, default="no address")
    path = models.CharField(max_length=60, blank=True)
    # image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.first_name
