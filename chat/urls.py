from django.urls import path
from .views import home_view, check_room, room

app_name = 'chat'

urlpatterns = [
    path( '', home_view, name='home-view' ),
    path( 'chat/', check_room, name='chat-room' ),
    path( '<str:room_name>/<str:username>', room, name='room' ),
]
