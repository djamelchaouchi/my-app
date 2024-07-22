from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html',)

@login_required
def timeline(request):
    return render(request, 'timeline.html',)


@login_required
def createpost(request):
    return render(request, 'create-post.html',)


@login_required
def chat(request):
    return render(request, 'chat.html',)


@login_required
def profile(request):
    return render(request, 'profile.html',)

@login_required
def userprofile(request):
    return render(request, 'user-profile.html',)

@login_required
def socialfriends(request):
    return render(request, 'social-friends.html',)

@login_required
def changepassword(request):
    return render(request, 'change-password.html',)



@login_required
def comment(request):
    return render(request, 'comment.html',)




@login_required
def editprofile(request):
    return render(request, 'edit-profile.html',)



# def error_404_view(request, exception):
    # return render(request, '404.html')



@login_required
def explore(request):
    return render(request, 'explore.html',)



def forgotpassword(request):
    return render(request, 'forgot-password.html',)




@login_required
def messagesdetail(request):
    return render(request, 'messages-detail.html',)



@login_required
def notification(request):
    return render(request, 'notification.html',)



@login_required
def reels(request):
    return render(request, 'reels.html',)

@login_required
def story(request):
    return render(request, 'story.html',)


@login_required
def livestory(request):
    return render(request, 'live-story.html',)

@login_required
def setting(request):
    return render(request, 'setting.html',)


def otpconfirm(request):
    return render(request, 'otp-confirm.html',)



@login_required
def security(request):
    return render(request, 'security.html',)


#@login_required
#def themesettings(request):
 #   return render(request, 'theme-settings.html',)