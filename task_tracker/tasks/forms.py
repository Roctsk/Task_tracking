from django import forms
from .models import Task, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','media']
        widgets = {
            "content":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Напишіть коментар..."
            })
        }
        {
            'media':forms.FileInput()
        }
        labels = {
            "content": ""
        }



class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "media"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title","description","status","priority","due_date"]
