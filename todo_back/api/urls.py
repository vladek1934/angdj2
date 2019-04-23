from django.urls import path
from api import views

urlpatterns = [

    path('api/task_lists/', views.Tasklists.as_view()),
    path('api/task_lists/<int:pk>/', views.Tasklist_detail.as_view()),
    path('api/task_lists/<int:pk>/tasks', views.Tasks.as_view()),
    path('api/tasks/<int:pk>', views.Task_detail.as_view())


]
