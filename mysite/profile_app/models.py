from django.db import models

class Profile(models.Model):
    # 基本情報
    name = models.CharField("名前", max_length=100)
    avatar_name = models.CharField("VRChatアバター名", max_length=100)
    top_image = models.ImageField("トップ画像", upload_to='images/', blank=True, null=True)
    icon_image = models.ImageField("アイコン画像", upload_to='icons/', blank=True, null=True)
    background_image = models.ImageField("背景画像", upload_to='backgrounds/', blank=True, null=True)

    # 自己紹介
    introduction = models.TextField("自己紹介文")
    reason_for_vrc = models.TextField("VRChatを始めた理由")
    
    # 趣味・好きなこと
    hobbies = models.TextField("趣味")
    favorite_things = models.TextField("好きなこと")

    # 将来の目標
    career_goal = models.CharField("目指している仕事", max_length=200)

    def __str__(self):
        return self.name