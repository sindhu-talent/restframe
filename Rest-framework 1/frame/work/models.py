from django.db import models
class Test(models.Model):
    name=models.CharField(max_length=25)
    branch=models.CharField(max_length=20)
    address=models.TextField()
    phoneno=models.IntegerField()
    def __str__(self):
        return self.name

# Create your models here.
