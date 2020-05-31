from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Wall(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length=60)
    body = models.TextField()
    published = models.DateTimeField(default = timezone.now)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title

