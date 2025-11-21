from django import forms
from django.contrib.auth.models import User
from .models import Task, Comment , UserProfile


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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["avatar","bio"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
