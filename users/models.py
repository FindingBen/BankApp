from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser


# class UserRole(AbstractUser):
#       BASIC = 1
#       SILVER = 2
#       GOLD =3
      
#       ROLE_CHOICES = (
#           (BASIC, 'Basic'),
#           (SILVER, 'Silver'),
#           (GOLD, 'Gold'),
#       )
#       role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.IntegerField(default=555333)
    userRank = models.CharField(default='Basic',max_length=10)

    def __str__(self):
        return f'{self.user.username} UserProfile'

   