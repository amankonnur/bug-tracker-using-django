from django.urls import path
from userapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('update',views.update,name='update'),
    path('logout',views.user_logout,name='logout'),
]