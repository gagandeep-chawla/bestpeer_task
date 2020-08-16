from django.db import models

# Create your models here.
class TodoList(models.Model):
    status_options = (
        ('Not Started','Not Started'),
        ('In Progress','In Progress'),
        ('Complete','Complete')
    )
    title = models.CharField(max_length=50)
    descripation = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices = status_options)

    def __str__(self):
        return self.status
    

