from django.contrib import admin
from main.models import User, Info
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _



@admin.register(User)
class UserAdmin(UserAdmin):
    list_display= ["id", "username", 'is_active', 'is_staff', 'is_superuser', 'city']
    fieldsets = (
        (None, {'fields':('username', 'password')}),
        (_('Permissions'), {
                'fields':('is_active', 'is_staff', "is_superuser",'user_permissions', 'city'),
        }),

    )

admin.site.register(Info)