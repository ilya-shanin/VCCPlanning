from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from accounts.forms import CustomUserChangeForm, SignUpForm

# Register your models here.

class AccontAdmin(UserAdmin):
    form = CustomUserChangeForm
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

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()

admin.site.register(CustomUser, AccontAdmin)