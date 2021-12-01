from django.contrib.auth.models import User
from django.db import models


# private room between 2 users
class PrivateChat( models.Model ):
    users = models.ManyToManyField( User, help_text='users in a private chat' )

    def __str__(self):
        return f'{self.users.first()} - {self.users.last()}'


# send request from one user to another and the private message created if the second one accepted
class PrivateRequest( models.Model ):
    from_user = models.ForeignKey( User, on_delete=models.CASCADE, help_text='user who send request',
                                   related_name='send_request' )
    to_user = models.ForeignKey( User, on_delete=models.CASCADE, help_text='user who receive request',
                                 related_name='receive_request', null=True )
    is_accepted = models.BooleanField( default=False )
    request_date = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return f'{self.from_user} --> {self.to_user}'


#  private messages
class PrivateMessage( models.Model ):
    private_chat = models.ForeignKey( PrivateChat, on_delete=models.CASCADE )
    message_text = models.CharField( max_length=2000, null=True )
    date_added = models.DateTimeField( auto_now_add=True )
    user = models.ForeignKey( User, on_delete=models.CASCADE )

    def __str__(self):
        return f'{self.user}'
