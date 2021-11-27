from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import LoginForm, RegisterForm


# login view implemented by function base view
def login_view(request):
    print(request.GET)
    if request.user.is_authenticated:
        return redirect( 'chat:home-view' )
    login_form = LoginForm( request.POST or None )
    if login_form.is_valid():
        username = login_form.cleaned_data.get( 'username' )
        password = login_form.cleaned_data.get( 'password' )
        user = authenticate( request, username=username, password=password )
        if user is not None:
            login( request, user )
            return redirect( 'chat:home-view' )
    context = {'login_form': login_form, 'title': 'Chat | Login'}
    return render( request, 'account/login-view.html', context )


# register view implemented by class base view
class RegisterView( View ):
    form_class = RegisterForm
    template_name = 'account/register-view.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect( 'home' )
        register_form = self.form_class()
        context = {
            'title': 'Chat | Register',
            'form': register_form
        }
        return render( request, self.template_name, context )

    def post(self, request):
        register_form = self.form_class( request.POST or None )
        print( register_form.is_valid(), request.method )
        if register_form.is_valid():
            username = register_form.cleaned_data.get( 'username' )
            email = register_form.cleaned_data.get( 'email' )
            password = register_form.cleaned_data.get( 'password' )
            new_user = User.objects.create_user( username=username, email=email, password=password )
            print( new_user )
            if new_user is not None:
                return redirect( 'account:login-user' )

        context = {
            'title': 'Chat | Register',
            'form': register_form
        }
        return render( request, self.template_name, context )


@login_required( login_url='account:login-user' )
def logout_user(request):
    logout( request )
    return redirect( 'account:login-user' )
