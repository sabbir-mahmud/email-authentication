# imports
from django.db import models
from django.contrib.auth import get_user_model


# get user models
User = get_user_model()


# profile user models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to='media/avatars/', null=True, blank=True)

    def __str__(self):
        return f'{self.user} Profile'
