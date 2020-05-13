from django.db import models


class student(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.IntegerField()
    date_re=models.DateField()
    degree=models.IntegerField()
    department=models.CharField(max_length=10)

    def __str__(self):
        return self.fname+"  "+self.lname+"  "+self.department