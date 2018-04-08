from django.db import models

class Reserve(models.Model):
    rollno=models.CharField(max_length=11)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)
    time=models.CharField(max_length=20)
