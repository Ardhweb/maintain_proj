from django.urls import path 

from . import views 

app_name='core'
urlpatterns = [
    path('', views.core_engine, name="home"),
    path('search/',views.search_user,name="search"),

]