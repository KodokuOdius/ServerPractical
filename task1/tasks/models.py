from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Низкий'),
        ('Medium', 'Средний'),
        ('High', 'Высокий'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Низкий')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_owner')
    assigner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='task_assigner')

    def __str__(self):
        return self.title
