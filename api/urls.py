from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('timesheets/lists/',views.TimeSheetListView.as_view(),name='timesheet_list'),
    path('timesheets/<pk>/update/',views.TimeSheetDetailView.as_view(),name='timesheet_detail'),
    path('timesheets/create',views.TimeSheetCreateView.as_view(),name='timesheet_create_entry'),
   
]