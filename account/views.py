from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
    context = {}
    return render( request, 'account/login-view.html', context )


def register_view(request):
    context = {}
    return render( request, 'account/register-view.html', context )


@login_required
def logout_user(request):
    logout( request )
    return redirect( 'chat:home-view' )
