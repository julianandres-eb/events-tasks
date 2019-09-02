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
    created_date = models.DateField('Creation Date', auto_now=True)
    changed_date = models.DateField('Date of Change', auto_now=True)
    start_date_time = models.DateTimeField('Start Date Time', null=True)
    end_date_time = models.DateTimeField('End Date Time', null=True)
    done = models.BooleanField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    event_id = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name_task