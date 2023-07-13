from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _


Group.add_to_class('max_limit_product', models.BigIntegerField(null=True, default=300, verbose_name=_('Max limit product')))
Group.add_to_class('max_limit_responsible', models.BigIntegerField(null=True, default=50, verbose_name=_('Max limit responsible')))
Group.add_to_class('max_limit_category', models.BigIntegerField(null=True, default=30, verbose_name=_('Max limit category')))
Group.add_to_class('max_limit_model', models.BigIntegerField(null=True, default=30, verbose_name=_('Max limit model')))
Group.add_to_class('max_limit_department', models.BigIntegerField(null=True, default=10, verbose_name=_('Max limit model')))
Group.add_to_class('ui', models.BooleanField(null=True, default=False, verbose_name=_('Building UI design')))


class CustomUser(AbstractUser):
    """This is custom user model"""

    class UserStatus(models.TextChoices):
        WORKER = 'wk', 'Worker'
        LEADER = 'lr', 'Leader'
        DEPUTY = 'dp', 'Deputy'
        DIRECTOR = 'dr', 'Director'
        VIEWER = 'vr', 'Viewer'

    status_member = models.CharField(max_length=3, choices=UserStatus.choices, verbose_name=_('User status'))
    description = models.CharField(max_length=128, verbose_name=_('Description'), blank=True, null=True)
    department = models.ForeignKey('Department', related_name='users', on_delete=models.PROTECT, blank=True, null=True)


class Department(models.Model):
    """ This is department model for organizations"""
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    group = models.ForeignKey(Group, on_delete=models.PROTECT)

    # def save(self, *args, **kwargs):
    #     if self.name != '':
    #         self.name = ' '.join(self.name.strip().split())
    #     super().save(self, *args, **kwargs)

    def __str__(self):
        return self.name