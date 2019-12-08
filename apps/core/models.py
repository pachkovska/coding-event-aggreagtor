from django.db import models


# Create your models here.
class repo_info(models.Model):
    project_name = models.CharField(max_length=160)
    location = models.CharField(max_length=160)
    github_link = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    github_username = models.CharField(max_length=160)
    repo_name = models.CharField(max_length=160)
    created = models.DateTimeField(auto_now_add=True)


