"""Making profiles for user's models without attached profile's models (different reasons)"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangopicsproj.settings")

import django

django.setup()

from django.contrib.auth.models import User
from profileapp.models import Profile

if __name__ == '__main__':
    users = User.objects.all()

    for u in users:
        try:
            Profile.objects.create(user=u, first_name=u.first_name, last_name=u.last_name)
        except:
            pass
