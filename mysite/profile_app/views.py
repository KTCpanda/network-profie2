from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

def profile_view(request):
    # データベースから最初のプロフィールを取得します。
    # もしプロフィールがまだ作成されていなければ、Noneが渡されます。
    profile = Profile.objects.first()
    return render(request, 'profile_app/profile.html', {'profile': profile})

def profile_edit_view(request):
    # 編集対象のプロフィールを取得します。
    # まだプロフィールが一つもなければ、新しく作成します。
    profile, created = Profile.objects.get_or_create(pk=1)

    if request.method == 'POST':
        # 送信されたデータとファイルを使ってフォームを検証します。
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # 保存が成功したら、プロフィールページにリダイレクトします。
            return redirect('profile')
    else:
        # 通常のアクセス（GETリクエスト）の場合、
        # 既存のプロフィール情報をフォームに表示します。
        form = ProfileForm(instance=profile)

    # フォームをテンプレートに渡して表示します。
    return render(request, 'profile_app/profile_edit.html', {'form': form})