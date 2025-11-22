from django.contrib import admin
from .models import Task , Comment ,CommentLike

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(CommentLike)

#Secret Key = ab2d5fb75d559ffd286c57fb187bf7e8