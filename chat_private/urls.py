from django.urls import path
from .views import private_chat

app_name = 'chat_private'

urlpatterns = [
    path( 'private_chat/<int:user_id>', private_chat, name='private-chat' )
]
