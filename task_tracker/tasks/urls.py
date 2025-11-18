from django.urls import path 
from .views import TaskListViews,TaskDetailView , TaskDeleteView, TaskUpdateView , like_comment,TaskCreateView , profile_view 
from tasks import views


urlpatterns = [
    path('',TaskListViews.as_view(),name="task_list"),
    path('<int:pk>',TaskDetailView.as_view(),name="task_detail"),
    path('<int:pk>/edit/',TaskUpdateView.as_view(),name="task_update"),
    path('<int:pk>/delete/',TaskDeleteView.as_view(),name="task_delete"),
    path('create/',TaskCreateView.as_view(),name="task_create"),
    path("like/<int:comment_id>/",like_comment, name="like_comment"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('comment/edit/<int:pk>/', views.CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/delete/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('profile/<str:username>/',profile_view , name='profile'),
]
