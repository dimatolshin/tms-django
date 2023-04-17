from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=20)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title