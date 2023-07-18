from io import BytesIO

from django.db import models
from django.core.files import File
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from PIL import Image, ImageDraw
import qrcode

from accounts.models import CustomUser
from .services import upload_image_path


class Category(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, verbose_name=_('name'))
    image = models.ImageField(upload_to='static/images', verbose_name=_('image'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Model(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(upload_to='static/images', verbose_name=_('image'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, verbose_name=_('name'), null=True, blank=True)
    schet = models.CharField(max_length=255, verbose_name=_('schet'), null=True, blank=True)
    category_id = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, blank=True, verbose_name=_('category_id'), null=True)
    room_number = models.CharField(max_length=30, verbose_name=_('room_number'), blank=True, null=True)
    inventar_number = models.CharField(max_length=255, unique=True, blank=True, verbose_name=_('inventar_number'))
    model_id = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, verbose_name=_('model_id'), null=True)
    responsible = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name=_('responsible'), blank=True, null=True)
    seria_number = models.CharField(max_length=70, blank=True, null=True, verbose_name=_('seria_number'))
    images = models.ImageField(upload_to=upload_image_path, verbose_name=_('images'), blank=True)
    status = models.IntegerField(null=True, default=1, verbose_name='status')
    description = models.TextField(verbose_name=_('description'), blank=True)
    year_of_manufacture = models.CharField(max_length=50, verbose_name=_('year_of_manufacture'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('updated_at'))

    def __str__(self) -> str:
        return str(self.inventar_number)

    # def save(self, *args, **kwargs):
    #     qr_image = qrcode.make(
    #         f"Inventar raqami: {self.inventar_number} \n Javobgar shaxs: {'Nomalum' if self.responsible_id is None else self.responsible_id.fullname } \n Xona: {self.room_number} \n ")
    #     qr_offset = Image.new('RGB', (570, 570), 'white')
    #     qr_offset.paste(qr_image)
    #     files_name = f'{self.inventar_number}---qrcode.png'
    #     stream = BytesIO()
    #     qr_offset.save(stream, 'PNG')
    #     self.qr_code.save(files_name, File(stream), save=False)
    #     qr_offset.close()
    #     super().save(*args, **kwargs)



class ActionHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=10)
    data = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    changed_model_name = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    inventar_number = models.CharField(max_length=255, blank=True, verbose_name=_('inventar_number'), null=True)

    def __str__(self):
        if self.user:
            text = f'{self.user.username}: {self.action}'
        else:
            text = f'unknown user: {self.action}'
        return text

