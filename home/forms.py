from django import forms
from home.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'post_slug']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        