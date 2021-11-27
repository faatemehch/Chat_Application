from django.urls import path
from .views import logout_user, login_view, RegisterView

app_name = 'account'

urlpatterns = [
    path( 'register', RegisterView.as_view(), name='register-user' ),
    path( 'login', login_view, name='login-user' ),
    path( 'logout', logout_user, name='logout-user' ),
]
