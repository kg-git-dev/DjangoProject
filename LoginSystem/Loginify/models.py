from django.db import models

# Create your models here.
class UserDetails(models.Model):
    """
    Represents a user in the system.
    """
    Username = models.CharField(max_length=50, primary_key=True)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12, blank=True)

    class Meta:
        verbose_name = "User Detail"
        verbose_name_plural = "User Details"

