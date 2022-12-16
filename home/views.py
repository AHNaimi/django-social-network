from django.shortcuts import render, redirect
from django.views import View
from home.models import Post, Comment
from home.forms import PostForm, CommentForm
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from accounts.models import UserModel
from django.http import HttpResponse
class HomePageView(View):
    def get(self, request):
        post = Post.objects.all()
        return render(request, 'home/home.html', {'post': post})


class PostView(View):
    form_comment = CommentForm

    def get(self, request, **kwargs):
        post = Post.objects.get(id=kwargs['post_id'])
        post_comment = post.pcomment.all()
        permission_comment = request.user != post.user
        return render(request, 'home/postpage.html',
                      {"post": post, 'pcomment': post_comment, 'form': self.form_comment, 'per_com': permission_comment})

    def post(self, request, **kwargs):
        form = self.form_comment(request.POST)
        post = Post.objects.get(id=kwargs['post_id'])
        post_comment = post.pcomment.all()
        if form.is_valid():
            post = Post.objects.get(id=kwargs['post_id'])
            comment = Comment(user=request.user, post=post, body=form.cleaned_data['body'])
            comment.save()
            messages.success(request, ' your comment was made successfully')
            return HttpResponseRedirect(self.request.path_info)
        return render(request, 'home/postpage.html', {"post": post, 'pcomment': post_comment, 'form': form})


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
        return render(request, 'home/postcreate.html', {'form': form})


class MyPostView(View):
    def get(self, request):
        user = request.user
        if user is None:
            messages.INFO(request, 'you have to login')
            return redirect('home:homepage')
        else:
            post = Post.objects.filter(user=user)
            # if post :
            return render(request, 'home/mypost.html', {'posts': post})
            # else:
            #     return render(request, 'home/mypost.html', {'posts': post})


class PostDeleteView(LoginRequiredMixin,View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if request.user.id == post.user.id:
            post.delete()
            messages.success(request, 'post deleted')
            user = request.user
            post_remain = Post.objects.filter(user=user)
            return render(request, 'home/mypost.html', {'posts': post_remain})
        return redirect('home:homepage')
