from django.contrib import admin

# Register your models here.
from .models import Project,TimeSheet

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'project_name']


@admin.register(TimeSheet)
class TimeSheetAdmin(admin.ModelAdmin):
  
    list_display = ['id']