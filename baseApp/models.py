from django.db import models

# Create your models here.
class AppUsers(models.Model):
    name = models.CharField(max_length=50, blank=False,default=None)
    lastaname = models.CharField(max_length=50, blank=False, default=None)
    email = models.EmailField(max_length=50, blank=False,default=None)

    def __str__(self):
        return (f"{self.name} {self.lastaname}")

