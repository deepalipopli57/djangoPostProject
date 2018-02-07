from django.utils import timezone

from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_on = models.DateTimeField()
    published_on = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_on = timezone.now()
        self.save()

    def __str__(self):
        return self.title
