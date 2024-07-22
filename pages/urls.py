from django.urls import path
from .import views
from django.contrib import admin
from .views import *



urlpatterns = [
path('', views.home, name='home' ),
path('timeline', views.timeline, name='timeline' ),
#path('theme-settings', views.themesettings, name='theme-settings' ),

path('create-post', views.createpost, name='create-post' ),
path('chat', views.chat, name='chat' ),
path('profile', views.profile, name='profile' ),
path('user-profile', views.userprofile, name='user-profile' ),
path('social-friends', views.socialfriends, name='social-friends' ),
path('change-password', views.changepassword, name='change-password' ),
path('comment', views.comment, name='comment' ),
path('edit-profile', views.editprofile, name='edit-profile' ),
path('explore', views.explore, name='explore' ),
path('forgot-password', views.forgotpassword, name='forgot-password' ),
path('messages-detail', views.messagesdetail, name='messages-detail' ),
path('notification', views.notification, name='notification' ),
path('reels', views.reels, name='reels' ),
path('story', views.story, name='story' ),
path('live-story', views.livestory, name='live-story' ),

path('setting', views.setting, name='setting' ),
path('otp-confirm', views.otpconfirm, name='otp-confirm' ),
path('security', views.security, name='security' ),
]