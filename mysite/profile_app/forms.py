from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'vrchat_id', 'twitter_url', 'discord_id', 'bio', 'icon_image', 'background_image']
