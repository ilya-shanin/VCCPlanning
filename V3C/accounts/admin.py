from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User
from accounts.forms import UserChangeForm, SignUpForm

# Register your models here.

class AccontAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = SignUpForm

    list_display = ('email', 
                'first_name', 
                'last_name', 
                'job', 
                'phonenumber', 
                'image', 
                'is_staff', 
                'is_superuser',
                'date_joined',
                'last_updated')
    list_filter = ('is_superuser', 'is_active')

    fieldsets = [
                (None,{'fields': ('email', 'password')}),
               ('Personal info',{'fields': ('image','first_name', 'last_name', 'job', 'phonenumber')}),
                ('Permissions', {'fields': ('is_staff', 'is_superuser')})
    ]    
    add_fieldsets = [
                (None,{'classes': ('wide'), 'fields': ('email', 'password1', 'password2', 'first_name', 'last_name')})
    ] 

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()

admin.site.register(User, AccontAdmin)