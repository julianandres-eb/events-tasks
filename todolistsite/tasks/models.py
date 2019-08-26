from django.db import models
from django.conf import settings


# Create your models here.

# PRIORITY
class Priority(models.Model):
    name_priority = models.CharField(max_length=200)

    def __str__(self):
        return self.name_priority


# TASK
class Task(models.Model):
    name_task = models.CharField(max_length=200)
    created_date = models.DateTimeField('Creation Date')
    changed_date = models.DateTimeField('Date of Change')
    done = models.BooleanField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name_task