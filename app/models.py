from django.db import models

# Create your models here.


class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.taskTitle
