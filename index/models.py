from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=30)
    uage = models.IntegerField()
    uemail = models.EmailField()

    def __str__(self):
        return self.uname
