from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects,name = 'projects'),
    path('project/<pk>/',views.project, name = 'single_project'),
    path('project/create',views.createProject,name='create-project'),
    path('project/<pk>/update',views.updateProject,name='update-project'),
    path('project/<pk>/delete',views.deleteProject,name='delete-project'),
]