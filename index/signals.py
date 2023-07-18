from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.forms.models import model_to_dict
from .middleware import get_current_request

from accounts.models import CustomUser, Department
from .models import ActionHistory, Category, Model, Product


# user signals
@receiver(post_save, sender=CustomUser)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        # Object is being created
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Created',
            data=instance.values(),
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_save, sender=CustomUser)
def user_pre_save(sender, instance, *args, **kwargs):
    if instance.id:
         # Object is being updated
        old_instance = sender.objects.get(pk=instance.pk)
        changed_fields = get_changed_fields(instance, old_instance)
        
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Updated',
            data=changed_fields,
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_delete, sender=CustomUser)
def user_pre_delete(sender, instance, **kwargs):
    user = get_current_request().user
    
    ActionHistory.objects.create(
        user=user,
        changed_model_name = instance._meta.model_name,
        action=f'Deleted',
        data=instance.values(),
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.pk,
    )


#department signals
@receiver(post_save, sender=Department)
def department_post_save(sender, instance, created, **kwargs):
    if created:
        user = get_current_request().user
        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Created',
            data=instance.values(),
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_save, sender=Department)
def department_pre_save(sender, instance, *args, **kwargs):
    if instance.id:
         # Object is being updated
        old_instance = sender.objects.get(pk=instance.pk)
        changed_fields = get_changed_fields(instance, old_instance)
        
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Updated',
            data=changed_fields,
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_delete, sender=Department)
def department_pre_delete(sender, instance, **kwargs):
    user = get_current_request().user
    
    ActionHistory.objects.create(
        user=user,
        changed_model_name = instance._meta.model_name,
        action=f'Deleted',
        data=instance.values(),
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.pk,
    )


# model signals
@receiver(post_save, sender=Model)
def model_post_save(sender, instance, created, **kwargs):
    if created:
        # Object is being created
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Created',
            data=instance.values(),
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_save, sender=Model)
def model_pre_save(sender, instance, *args, **kwargs):
    if instance.id:
         # Object is being updated
        old_instance = sender.objects.get(pk=instance.pk)
        changed_fields = get_changed_fields(instance, old_instance)
        
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Updated',
            data=changed_fields,
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_delete, sender=Model)
def model_pre_delete(sender, instance, **kwargs):
    user = get_current_request().user
    
    ActionHistory.objects.create(
        user=user,
        changed_model_name = instance._meta.model_name,
        action=f'Deleted',
        data=instance.values(),
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.pk,
    )


# category 
@receiver(post_save, sender=Category)
def category_post_save(sender, instance, created, **kwargs):
    if created:
        # Object is being created
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Created',
            data=instance.values(),
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_save, sender=Category)
def category_pre_save(sender, instance, *args, **kwargs):
    if instance.id:
         # Object is being updated
        old_instance = sender.objects.get(pk=instance.pk)
        changed_fields = get_changed_fields(instance, old_instance)
        
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Updated',
            data=changed_fields,
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_delete, sender=Category)
def category_pre_delete(sender, instance, **kwargs):
    user = get_current_request().user
    
    ActionHistory.objects.create(
        user=user,
        changed_model_name = instance._meta.model_name,
        action=f'Deleted',
        data=instance.values(),
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.pk,
    )


# product signals
@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    if created:
        # Object is being created
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Created',
            data=instance.values(),
            inventar_number = instance.inventar_number,
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_save, sender=Product)
def product_pre_save(sender, instance, *args, **kwargs):
    if instance.id:
         # Object is being updated
        old_instance = sender.objects.get(pk=instance.pk)
        changed_fields = get_changed_fields(instance, old_instance)
        
        user = get_current_request().user

        ActionHistory.objects.create(
            user=user,
            changed_model_name = instance._meta.model_name,
            action=f'Updated',
            data=changed_fields,
            inventar_number = instance.inventar_number,
            content_type=ContentType.objects.get_for_model(sender),
            object_id=instance.pk,
        )


@receiver(pre_delete, sender=Product)
def product_pre_delete(sender, instance, **kwargs):
    user = get_current_request().user
    
    ActionHistory.objects.create(
        user=user,
        changed_model_name = instance._meta.model_name,
        action=f'Deleted',
        data=instance.values(),
        content_type=ContentType.objects.get_for_model(sender),
        object_id=instance.pk,
    )



def get_user_from_request(request):
    if request.user.is_authenticated:
        return request.user
    else:
        return None


def get_changed_fields(new_instance, old_instance):
    changed_fields = {}
    new_values = model_to_dict(new_instance)
    old_values = model_to_dict(old_instance)
    for field, value in new_values.items():
        if value != old_values[field]:
            changed_fields[field] = value
    return changed_fields
