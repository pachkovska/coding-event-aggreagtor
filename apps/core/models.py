from django.db import models


# Create your models here.
class Repo_info(models.Model):
    project_name = models.CharField(max_length=160)
    location = models.CharField(max_length=160)
    github_link = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    


