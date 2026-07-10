from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    branch = models.CharField(max_length=100)
    cgpa = models.FloatField()
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)