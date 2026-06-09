from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('profile/', views.profile, name='profile'),

    path('create-post/', views.create_post, name='create_post'),

    path('like/<int:id>/', views.like_post, name='like_post'),

    path('comment/<int:id>/', views.add_comment, name='add_comment'),

    path('delete-comment/<int:id>/', views.delete_comment, name='delete_comment'),

    path('follow/<int:id>/', views.follow_user, name='follow_user'),
]