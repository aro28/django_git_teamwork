from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Employee(models.Model):
    f_name = models.CharField(max_length=20)
    b_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name
