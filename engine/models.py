from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    branch = models.CharField(max_length=100, blank=True)
    cgpa = models.FloatField(null=True, blank=True)

    resume = models.FileField(upload_to='resumes/')

    # AI Analysis Data
    resume_summary = models.TextField(blank=True)

    detected_skills = models.JSONField(default=list, blank=True)
    missing_skills = models.JSONField(default=list, blank=True)

    recommended_careers = models.JSONField(default=list, blank=True)
    roadmap = models.JSONField(default=list, blank=True)

    recommended_courses = models.JSONField(default=list, blank=True)
    recommended_jobs = models.JSONField(default=list, blank=True)

    improvement_suggestions = models.JSONField(default=list, blank=True)

    ats_score = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"