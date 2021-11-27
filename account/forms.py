from django import forms
from django.contrib.auth.models import User


class LoginForm( forms.Form ):
    username = forms.CharField(
        widget=forms.TextInput( attrs={'type': 'text', 'class': 'form-control', 'aria-describedby': 'emailHelp'} ) )
    password = forms.CharField( widget=forms.PasswordInput( attrs={'type': 'password', 'class': 'form-control',
                                                                   'aria-describedby': 'passwordHelp'} ) )

    def clean_username(self):
        username = self.cleaned_data.get( 'username' )
        user_exist = User.objects.filter( username=username ).exists()
        if not user_exist:
            raise forms.ValidationError( 'Enter the correct username!' )
        return username

    # def clean_password(self):
    #     username = self.cleaned_data.get( 'username' )
    #     password = self.cleaned_data.get( 'password' )
    #     user_exist = User.objects.filter( username=username, password=password ).exists()
    #     if not user_exist:
    #         return forms.ValidationError( 'Enter your correct information!' )
    #     return password


class RegisterForm( forms.Form ):
    username = forms.CharField(
        widget=forms.TextInput( attrs={'type': 'text', 'class': 'form-control', 'aria-describedby': 'emailHelp'} ),
        required=True, )

    email = forms.CharField(
        widget=forms.EmailInput( attrs={'type': 'email', 'class': 'form-control', 'aria-describedby': 'emailHelp'} ),
        required=True, )

    password = forms.CharField( widget=forms.PasswordInput( attrs={'type': 'password', 'class': 'form-control',
                                                                   'aria-describedby': 'passwordHelp'} ),
                                required=True, )
    re_password = forms.CharField( widget=forms.PasswordInput( attrs={'type': 'password', 'class': 'form-control',
                                                                      'aria-describedby': 'repasswordHelp'} ),
                                   required=True, )

    def clean_username(self):
        username = self.cleaned_data.get( 'username' )
        user_exist = User.objects.filter( username=username ).exists()
        if user_exist:
            raise forms.ValidationError( 'Enter the correct username!' )
        return username

    def clean_email(self):
        email = self.cleaned_data.get( 'email' )
        is_exist_email = User.objects.filter( email=email ).exists()
        if is_exist_email:
            raise forms.ValidationError( 'Change Your Email Address!' )
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get( 'password' )
        re_password = self.cleaned_data.get( 're_password' )
        if password != re_password:
            raise forms.ValidationError( 'passwords must be matched!' )
        return re_password
