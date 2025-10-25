from django.urls import path 
from .views import TaskListViews,TaskDeleteView


urlpatterns = [
    path('',TaskListViews.as_view(),name="task_list"),
    path('<int:pk>',TaskDeleteView.as_view(),name="task_detail"),
]
