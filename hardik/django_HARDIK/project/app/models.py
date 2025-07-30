from django.db import models

# Create your models here.
class Creation(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Status(models.TextChoices):
    PENDING = 'pending', 'pending'
    IN_PROGRESS = 'in-progress','in-progress'
    FINISHED = 'finished', 'finished'

class Note(Creation):
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
