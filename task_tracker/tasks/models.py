
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICE = [
        ("do","Нове"),
        ("in_progress","В процесі"),
        ("completed","Завершено"),
    ]

    PRIORRITY_CHOICE = [
        ("low","Низький"),
        ("medium","Середній"),
        ("high","Високий"),
    ]

    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default="do")
    priority = models.CharField(max_length=20,choices=PRIORRITY_CHOICE,default="medium")
    due_date = models.DateField(verbose_name="Термін воконання",null=True,blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-create_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["create_at"]

    def __str__(self):
        return f"Коментар від {self.author.username} до {self.task.title}"
    

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="likes")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ("comment" ,"user")
