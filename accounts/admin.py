from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile
from django.utils.html import format_html


class UserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = []
    list_filter = []
    fieldsets = []


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="/media/{}" alt="{}" width="30" style="border-radius: 50%;">'.format(object.profile_picture, object.user.username))
    thumbnail.short_description = 'Foto de perfil'

    list_display = ['thumbnail', 'user', 'city', 'state', 'country']
    list_display_links = ['user']


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)