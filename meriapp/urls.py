from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('blogpost', views.blogpost, name='blogpost'),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('blog_detail/delete/<int:id>', views.delete_post, name='delete_post'),
    path('blog_detail/edit/<int:id>', views.edit_post, name='edit_post'),
    path('contact_form', views.contact_form , name='contact_form'),
    path('change_password', views.change_password , name='change_password'),
]