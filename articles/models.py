from django.db import models

from django.contrib import admin


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=20)
    like_count = models.IntegerField(default=0)

    @admin.display(
        boolean=True,
        description="Is popular?",
        ordering='like_count'
    )
    def is_popular(self):
        return self.like_count >= 100

    def __str__(self):
        return self.title