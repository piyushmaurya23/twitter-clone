from django.db import models
from twitter.users.models import User

# Create your models here.


class Tweet(models.Model):
    content = models.TextField(max_length=140)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='tweets/%d/', blank=True)

    def __str__(self):
        return self.user


