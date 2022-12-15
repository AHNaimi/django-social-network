from django import forms
from home.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_slug']