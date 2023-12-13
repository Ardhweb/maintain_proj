from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import uuid

class Project(models.Model):
    project_id = models.CharField(max_length=255, default=uuid.uuid4().hex[:12], editable=False)
    project_name = models.CharField(max_length=50,blank=False)
    description =  models.TextField(blank=False,max_length=540)
    started_at = models.DateField(blank=True,null=True)
    end_at = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(blank=True,auto_now_add=True)
    #auto_now_add for automatic add firsttime when it object created so it not change even how many time we 
    updated_at = models.DateTimeField(blank=True,auto_now=True)
    #auto_now is for whenever this we chnage anything in object it will update the date time and store it to updated_at

    def __str__(self):
        return f"{self.project_name},{self.project_id}"
    
class TimeSheet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project,blank=True)
    week_start_date = models.DateField(blank=True,null=True)
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.id}{self.user.username}"
    