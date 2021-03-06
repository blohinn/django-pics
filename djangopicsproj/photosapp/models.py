from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.URLField()
    caption = models.TextField(max_length=300, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published',)