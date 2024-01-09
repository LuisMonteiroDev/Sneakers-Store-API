from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
    filter_horizontal = ['favorite_brands', 'favorite_sneakers']


admin.site.register(UserProfile, UserProfileAdmin)

