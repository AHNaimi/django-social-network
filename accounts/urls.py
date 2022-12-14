from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='registerpage'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='loginpage')

]
