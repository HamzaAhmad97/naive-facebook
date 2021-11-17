from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse

class Post(models.Model):
    content = models.TextField()
    added_by = models.ForeignKey(get_user_model(),
        null=True, blank=True, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:15]

    def get_absolute_url(self):
        return reverse('posts_list')