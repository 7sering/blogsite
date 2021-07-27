from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('addblog/' , addblog, name='addblog'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('blog_detail/<slug>', blog_detail, name='blog_detail'),
    path('all-blogs/', all_blogs, name='all_blogs'),
    path('blog-delete/<id>/', delete_blog, name='delete_blogs'),
    path('blog-update/<id>', blog_update, name='blog_update'),
]