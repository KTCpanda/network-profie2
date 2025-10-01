from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'avatar_name']
    fieldsets = (
        ('基本情報', {
            'fields': ('name', 'avatar_name')
        }),
        ('画像設定', {
            'fields': ('top_image', 'icon_image', 'background_image')
        }),
        ('プロフィール内容', {
            'fields': ('introduction', 'reason_for_vrc', 'hobbies', 'favorite_things', 'career_goal')
        }),
    )