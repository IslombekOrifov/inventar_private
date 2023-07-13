import sys
import random 

from django.core.management.base import BaseCommand, CommandError

from accounts.models import CustomUser
from index.models import Category

class Command(BaseCommand):
    help = 'Add category dump data'

    def handle(self, *args, **options):
        superuser = CustomUser.objects.get(username='admin1')

        a = list((Category(name=f'Category {i} ', group=superuser.groups.first()) for i in range(1,20)))
        Category.objects.bulk_create(a)
        print('done')