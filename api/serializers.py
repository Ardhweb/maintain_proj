from rest_framework import serializers
from core.models import Project , TimeSheet

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        
class TimeSheetSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)
    class Meta:
        model = TimeSheet
        fields = ['id','projects','user','week_start_date','hours_worked']
       