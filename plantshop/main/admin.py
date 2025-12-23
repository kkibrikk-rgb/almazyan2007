from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Plant

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'created_at')
    list_filter = ('in_stock',)
    search_fields = ('name', 'description')
