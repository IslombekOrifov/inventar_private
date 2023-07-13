import sys
import random 

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

from accounts.models import CustomUser, Department

class Command(BaseCommand):
    help = 'Add users'
    args = '[count]'

    def handle(self, count=1000, *args, **options):
        user = list(CustomUser.objects.exclude(id=1).values_list('id', flat=True))
        print(user)
        group = Group.objects.all().first()
        group.user_set.add(*user)
        