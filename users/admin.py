from django.contrib import admin
from .models import UserModel
from django.forms import TextInput, Textarea, CharField
from django.db import models


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    search_fields = ('email', 'user_name', 'full_name',)
    list_filter = ('email', 'user_name', 'full_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'full_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'full_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
