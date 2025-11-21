import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_tracker.settings')

import django
django.setup()

from tasks.models import UserProfile
from django.contrib.auth.models import User

user = User.objects.get(username='user1')

profile = UserProfile.objects.create(user=user, avatar='default_avatar.jpg', bio='Біографія адміністратора')
print("Профіль для користувача 'admin' створено!")
