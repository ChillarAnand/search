from django.db import models


class Document(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    data = models.TextField()

    def __str__(self):
        return self.title
