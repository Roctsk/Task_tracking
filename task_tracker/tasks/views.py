from django.shortcuts import render,redirect , get_object_or_404
from django.views.generic import ListView  ,DetailView, DeleteView, UpdateView
from .models import Task , Comment, CommentLike
from django.urls import reverse_lazy
from .forms import CommentForm
from django.db.models import Count

from django.contrib.auth.decorators import login_required


class TaskListViews(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = CommentForm()

        context["comments"] = Comment.objects.annotate(
            like_count=Count("likes")
        ).order_by("-like_count", "-create_at")

        return context

    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")

        form = CommentForm(request.POST)
        if form.is_valid():
            task_id = request.POST.get("task_id")
            try:
                task = Task.objects.get(pk=task_id)
            except Task.DoesNotExist:
                return redirect("task_list")

            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
        return redirect("task_list")


@login_required
def like_comment(request,comment_id):
    comment = get_object_or_404(Comment, id = comment_id)

    like,created = CommentLike.objects.get_or_create(
        comment = comment,
        user = request.user
    )

    if not created:
        like.delete()

    return redirect("task_list")





class TaskDetailView(DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    context_object_name = "task"
        

class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title","description", "status", "priority", "due_date"]
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    context_object_name = "task"
    success_url = reverse_lazy("task_list")


