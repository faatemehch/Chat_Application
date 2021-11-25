from django.urls import path
from .views import logout_user, login_view, register_view

app_name = 'account'

urlpatterns = [
    path( 'logout', logout_user, name='logout-user' ),
    path( 'login', login_view, name='login-user' ),
    path( 'register', register_view, name='register-user' )
]
