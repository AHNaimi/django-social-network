from django.urls import path
from home import views


app_name = 'home'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('post/<int:post_id>/<slug:post_slug>', views.PostView.as_view(),  name='postpage'),
    path('post/create', views.PostCreateView.as_view(), name='postcreatepage'),
    path('post/mypost', views.MyPostView.as_view(), name='mypostpage'),
    path('post/delete/<int:post_id>', views.PostDeleteView.as_view(), name='deletepost'),
    path('post/update/<int:post_id>', views.PostUpdateView.as_view(), name='updatepost')
]