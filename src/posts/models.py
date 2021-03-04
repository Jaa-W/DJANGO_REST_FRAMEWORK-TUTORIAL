from django.db import models

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)       # Automatic saving time of created post 
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created']                              # Ordering by date of creating posts 
