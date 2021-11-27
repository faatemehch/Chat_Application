from django.urls import path, include
from django.contrib.auth import views as forogotpassword_view

app_name = 'forgot_password'

urlpatterns = [
    path( 'password-reset/', forogotpassword_view.PasswordResetView.as_view(
        template_name='forgot_password/password_reset_form.html',
        email_template_name='forgot_password/password_reset_email.html',
        subject_template_name='forgot_password/password_reset_subject.txt'
    ),
          name='password_reset' ),

    path( 'password-reset/done/', forogotpassword_view.PasswordResetDoneView.as_view(
        template_name='forgot_password/password_reset_done.html'
    ), name='password_reset_done' ),

    path( 'password-reset-confirm/<uidb64>/<token>/',
          forogotpassword_view.PasswordResetConfirmView.as_view(
              template_name='forgot_password/password_reset_confirm.html'
          ),
          name='password_reset_confirm' ),

    path( 'password-reset-complete/',
          forogotpassword_view.PasswordResetCompleteView.as_view(
              template_name='forgot_password/password_reset_complete.html'
          ),
          name='password_reset_complete' ),

]
