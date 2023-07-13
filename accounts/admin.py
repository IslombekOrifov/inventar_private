from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from .models import CustomUser, Department

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin): 
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",),},),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Status and description"), {"fields": ("status_member", "description", "department")}),
    )


@admin.register(Department)
class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    search_fields = ['name']
    list_filter = ['group']