from django.db import models
from django.contrib.auth.models import User

class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credentials')
    website_url = models.URLField(max_length=255)
    login