from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    university = models.CharField(max_length=20)

    def __str__(self):
        return self.name
