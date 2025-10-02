from django.shortcuts import render
# from .models import Profile # models.py をまだ使用していないためコメントアウト
# from .forms import ProfileForm # forms.py をまだ使用していないためコメントアウト

def profile_view(request):
    # ここにあなたの情報を直接書き込んでください！
    my_profile = {
        'name': 'moepanda(萌ぱんだ)',
        'avatar_name': '萌ぱんだ',
        'top_image_url': 'images/avatar.jpg', # 表示したい画像のパス


        'introduction': """
            僕は萌ぱんだです！
        元気があるのが僕のいいところ学校ではぱんだマンって言われてます
        　vrchatは9/29に始めたばっかりですそのついでにvrchatでプロフィールにリンク貼れるので
        自己紹介サイトを作ってみた感じです！
        """,
        'reason_for_vrc': """
        YouTubeやTikTokでなかのっちチャンネルというYouTubeが面白く会話してたので始めました
        今はデスクトップですがメタクエ欲しいと思ってます
        """,
        'hobbies': """
            趣味は服を買ったり化粧品を買うことです
        メイクはまだ全然手をつけてないですが肌を綺麗になるように頑張ってます
        自分の好きな服は和装系と地雷系です
        """,
        'favorite_things': """
        ゲームと人と日常会話を話すことです
        vrchatではどっちもできるので最高です:thumbsup:
        たまに狂ってる人いるけど…
        """,
        'career_goal': '目指してる仕事はまだ決まってませんがゲーム系のエンジニアになりたいです'
    }
    
    # 'profile'という名前で、上の my_profile の情報をHTMLに渡します
    return render(request, 'profile_app/profile.html', {'profile': my_profile})