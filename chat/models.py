from django.contrib.auth.models import User
from django.db import models


class Room( models.Model ):
    room_name = models.CharField( max_length=200, help_text='name of room' )

    def __str__(self):
        return self.room_name


class Message( models.Model ):
    owner = models.ForeignKey( User, on_delete=models.CASCADE )
    message_text = models.CharField( max_length=1000 )
    date_added = models.DateTimeField( auto_now_add=True, help_text='message date and time' )
    room = models.ForeignKey( 'Room', on_delete=models.CASCADE, null=True )

    def __str__(self):
        return self.owner.username
