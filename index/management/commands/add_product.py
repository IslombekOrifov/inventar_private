import sys
import random 
from uuid import uuid4

from django.core.management.base import BaseCommand, CommandError

from accounts.models import CustomUser
from index.models import Category, Product, Model


class Command(BaseCommand):
    
    def handle(self, count=1000, *args, **options):
        superuser = CustomUser.objects.filter(username='admin1').first()
        users = CustomUser.objects.filter(is_superuser=False)
        categories = Category.objects.filter(group=superuser.groups.first())
        modellar = Model.objects.filter(group=superuser.groups.first())
        desc = """fringilla ut morbi tincidunt augue interdum velit euismod 
            in pellentesque massa placerat duis ultricies lacus sed turpis tincidunt 
            id aliquet risus feugiat in ante metus dictum at tempor commodo ullamcorper 
            a lacus vestibulum sed arcu non odio euismod lacinia at quis risus sed 
            vulputate odio ut enim blandit volutpat maecenas volutpat blandit aliquam 
            etiam erat velit scelerisque in dictum non consectetur a erat nam at lectus 
            urna duis convallis convallis tellus id interdum velit laoreet id donec 
            ultrices tincidunt arcu
        """
        
        a = list((Product(group=superuser.groups.first(), name=f'Product {random.randint(1, 11000000)}', schet=str(random.randint(1, 11000000)), room_number=str(random.randint(1, 500)), inventar_number=str(uuid4()), category_id=cat, model_id=mod, responsible=user, seria_number=str(random.randint(1, 11000000)), description=desc, year_of_manufacture=str(random.randint(2015, 2023)),) for user in users for cat in categories for mod in modellar))
        Product.objects.bulk_create(a)
        print('done')
