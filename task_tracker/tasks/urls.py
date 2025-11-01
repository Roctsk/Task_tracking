from django.urls import path 
from .views import TaskListViews,TaskDetailView , TaskDeleteView, TaskUpdateView , like_comment,TaskCreateView


urlpatterns = [
    path('',TaskListViews.as_view(),name="task_list"),
    path('<int:pk>',TaskDetailView.as_view(),name="task_detail"),
    path('<int:pk>/edit/',TaskUpdateView.as_view(),name="task_update"),
    path('<int:pk>/delete/',TaskDeleteView.as_view(),name="task_delete"),
    path('create/',TaskCreateView.as_view(),name="task_create"),
    path("like/<int:comment_id>/",like_comment, name="like_comment"),
]
