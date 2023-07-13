import sys
import random 

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password

from accounts.models import CustomUser, Department

class Command(BaseCommand):
    help = 'Add users'
    args = '[count]'

    def handle(self, count=1000, *args, **options):
        superuser = CustomUser.objects.get(username='admin1')
        department = Department.objects.filter(group=superuser.groups.first())
        
        desc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do \
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad \
            minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip \
            ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate \
            velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \
            non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        
        # create directors
        son = 0
        a = list((CustomUser(username=f'name{random.randint(1, 1000000)}abc@gmail.com', password=make_password('admin12345'), first_name=f'name {random.randint(1, 1000000)}abc', last_name=f'last name {random.randint(1, 1000000)}abc', email=f'name{random.randint(1, 1000000)}abc@gmail.com', description=desc, status_member=CustomUser.UserStatus.DIRECTOR, department=i) for i in department))
        CustomUser.objects.bulk_create(a)
        print('done')

        # create deputys
        a = list((CustomUser(username=f'name{random.randint(1, 1000000)}abc@gmail.com', password=make_password('admin12345'), first_name=f'name {random.randint(1, 1000000)}abc', last_name=f'last name {random.randint(1, 1000000)}abc', email=f'name{random.randint(1, 1000000)}abc@gmail.com', description=desc, status_member=CustomUser.UserStatus.DEPUTY, department=i) for i in department))
        CustomUser.objects.bulk_create(a)
        print('done')

        # create leaders
        a = list((CustomUser(username=f'name{random.randint(1, 1000000)}abc@gmail.com', password=make_password('admin12345'), first_name=f'name {random.randint(1, 1000000)}abc', last_name=f'last name {random.randint(1, 1000000)}abc', email=f'name{random.randint(1, 1000000)}abc@gmail.com', description=desc, status_member=CustomUser.UserStatus.LEADER, department=depart) for depart in department for i in range(1,5)))
        CustomUser.objects.bulk_create(a)
        print('done')

        # create workers
        a = list((CustomUser(username=f'name{random.randint(1, 1000000)}abc@gmail.com', password=make_password('admin12345'), first_name=f'name {random.randint(1, 1000000)}abc', last_name=f'last name {random.randint(1, 1000000)}abc', email=f'name{random.randint(1, 1000000)}abc@gmail.com', description=desc, status_member=CustomUser.UserStatus.WORKER, department=depart) for depart in department for i in range(1,11)))
        CustomUser.objects.bulk_create(a)
        print('done')

        # create viewers
        a = list((CustomUser(username=f'name{random.randint(1, 1000000)}abc@gmail.com', password=make_password('admin12345'), first_name=f'name {random.randint(1, 1000000)}abc', last_name=f'last name {random.randint(1, 1000000)}abc', email=f'name{random.randint(1, 1000000)}abc@gmail.com', description=desc, status_member=CustomUser.UserStatus.VIEWER) for i in range(370,372)))
        CustomUser.objects.bulk_create(a)
        print('done')

        