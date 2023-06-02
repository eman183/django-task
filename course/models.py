from django.db import models

# Create your models here.
class Course (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name