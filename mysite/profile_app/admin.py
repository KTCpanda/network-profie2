from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'vrchat_id')
    fieldsets = (
        ('基本情報', {
            'fields': ('name', 'vrchat_id', 'twitter_url', 'discord_id')
        }),
        ('自己紹介', {
            'fields': ('bio',)
        }),
        ('画像', {
            'fields': ('icon_image', 'background_image')
        }),
    )