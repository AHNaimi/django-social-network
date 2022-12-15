from django.shortcuts import render, redirect
from django.views import View
from home.models import Post, Comment
from home.forms import PostForm, CommentForm
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class HomePageView(View):
    def get(self, request):
        post = Post.objects.all()
        return render(request, 'home/home.html', {'post': post})


class PostView(View):
    form_comment = CommentForm

    def get(self, request, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'])
        pcomment =post.pcomment.all()
        return render(request, 'home/postpage.html', {"post": post, 'pcomment': pcomment, 'form': self.form_comment})

    def post(self, request, **kwargs):
        pass
        # form = self.form_comment(request.POST)
        # if form.is_valid():
        #     post = Post.objects.get(id=kwargs['post_id'])
        #     comment = Comment(user=request.user, post=post, body=form.cleaned_data['body'])
        #     comment.save()


class PostCreateView(LoginRequiredMixin, View):
    form_class = PostForm

    def get(self, request):
        return render(request, 'home/postcreate.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], body=form.cleaned_data['body'], user=request.user,
                        post_slug=slugify(form.cleaned_data['title'][:20]))
            post.save()
            messages.success(request, 'your post created successfully')
            return redirect('home:homepage')
