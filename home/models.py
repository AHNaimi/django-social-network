from django.db import models
from accounts.models import UserModel
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_post')
    title = models.CharField(max_length=50)
    post_slug = models.SlugField()
    body = models.TextField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home:postpage', args=(self.id, self.post_slug))
