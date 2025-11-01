from django import forms
from .models import Comment , Task

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            "content":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Напишіть коментар..."
            })
        }
        labels = {
            "content": ""
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title","description","status","priority","due_date"]
