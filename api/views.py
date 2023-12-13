from rest_framework import generics
from core.models import Project, TimeSheet
from .serializers import ProjectSerializer,TimeSheetSerializer
from django.contrib.auth.models import User
from rest_framework import mixins
#Retrieving a list of timesheet entries for a specific user
#Ensure that users can only view and edit their own timesheet entries.
from rest_framework.views import APIView
from rest_framework.response import Response


class TimeSheetCreateView(generics.ListAPIView,mixins.CreateModelMixin):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return TimeSheet.objects.filter(user=user)
        else:
            return TimeSheet.objects.none()
            
    def post(self, request, *args, **kwargs):
        data = request.data
        projects= request.data.get("projects")
        user = request.user
        week_start_date = request.data.get("week_start_date")
        hours_worked = request.data.get("hours_worked")
        time_sheet = TimeSheet.objects.create(user=user, week_start_date=week_start_date, hours_worked=hours_worked)

         # Link TimeSheet with Projects
        for project_id in projects:
            try:
                project = Project.objects.get(pk=project_id)
                time_sheet.projects.add(project)
            except Project.DoesNotExist:
                raise serializers.ValidationError({"projects": f"Project with ID {project_id} not found."})
        # Serialize and return created TimeSheet
        serializer = TimeSheetSerializer(time_sheet)
        return Response(serializer.data)

 


class TimeSheetListView(generics.ListAPIView):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return TimeSheet.objects.filter(user=user)
        else:
            return TimeSheet.objects.none()
    

class TimeSheetDetailView(generics.RetrieveAPIView,mixins.UpdateModelMixin,):
    queryset = TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return TimeSheet.objects.filter(user=user)
        else:
            return TimeSheet.objects.none()
    
    def put(self, request, pk, *args, **kwargs):
        try:
            time_sheet = TimeSheet.objects.get(pk=pk)
        except TimeSheet.DoesNotExist:
            return Response({"error": "TimeSheet not found."}, status=status.HTTP_404_NOT_FOUND)
            # Update user, week_start_date, and hours_worked if provided
        data = request.data
        if data.get("user"):
            # time_sheet.user = data["user"]
            time_sheet.user = request.user
           
        if data.get("week_start_date"):
            time_sheet.week_start_date = data["week_start_date"]
        if data.get("hours_worked"):
            time_sheet.hours_worked = data["hours_worked"]
            # Update projects
        projects = data.get("projects")
        if projects is not None:
             # Clear existing projects
            time_sheet.projects.clear()
            # Link provided projects
            for project_id in projects:
                try:
                    project = Project.objects.get(pk=project_id)
                    time_sheet.projects.add(project)
                except Project.DoesNotExist:
                    return Response({"projects": f"Project with ID {project_id} not found."}, status=status.HTTP_400_BAD_REQUEST)
                    # Save the updated TimeSheet
        time_sheet.save()
        serializer = TimeSheetSerializer(time_sheet)
        return Response(serializer.data)
