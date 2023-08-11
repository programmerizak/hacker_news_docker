from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username','email', 'can_post','date_joined',]
    list_editable = ['can_post']
    ordering = ['-date_joined']
    fieldsets = UserAdmin.fieldsets + (
            ('User Informations', {'fields': (
            	'little_about_you','profile_picture')}),
            ('Permissions', {'fields': ('can_post',)}),

    )
admin.site.register(User, UserAdmin)
