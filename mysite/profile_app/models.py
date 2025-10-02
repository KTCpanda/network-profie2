from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    #top_image = CloudinaryField('image', blank=True, null=True)
    # 基本情報
    name = models.CharField("名前", max_length=100, default="名無しさん")
    vrchat_id = models.CharField("VRChat ID", max_length=100, blank=True)
    twitter_url = models.URLField("Twitter URL", max_length=200, blank=True)
    discord_id = models.CharField("Discord ID", max_length=100, blank=True)
    
    # 自己紹介
    bio = models.TextField("自己紹介文", blank=True)

    # 画像
    icon_image = models.ImageField("アイコン画像", upload_to='images/', blank=True, null=True)
    background_image = models.ImageField("背景画像", upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name