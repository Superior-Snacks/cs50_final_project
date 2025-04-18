from django.db import models
from django.contrib.auth.models import User

class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credentials')
    website_url = models.URLField(max_length=255)
    login = models.CharField(max_length=255)
    encrypted_password = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.website_urk} ({self.login})"