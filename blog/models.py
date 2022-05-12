from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    public = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


