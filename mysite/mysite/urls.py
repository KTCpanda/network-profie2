# f:\network-profie2\mysite\mysite\urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 追加
from django.conf.urls.static import static # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profile_app.urls')),
]

# 開発環境(DEBUG=True)のときだけ、メディアファイルのURLを有効にする
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)