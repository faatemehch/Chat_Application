from django.urls import path
from .views import home_view, check_room, room, send_message, get_messages

app_name = 'chat'

urlpatterns = [
    path( '', home_view, name='home-view' ),
    path( 'chat-room/', check_room, name='chat-room' ),
    path( '<str:room_name>/', room, name='room' ),
    path( 'send_message', send_message, name='send_message' ),
    path( 'get_messages/<str:room_name>', get_messages, name='get_messages' ),
]
