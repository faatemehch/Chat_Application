from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


# private room between 2 users
class PrivateRoom( models.Model ):
    users = models.ManyToManyField( User, help_text='users in a private chat' )
    is_accepted = models.BooleanField( default=False, help_text='to create a start private chat between two user' )

    def __str__(self):
        return f'{self.users.first()} -{self.users.last()}'


#  private messages
class PrivateMessage( models.Model ):
    private_room = models.ForeignKey( PrivateRoom, on_delete=models.CASCADE )
    message_text = models.CharField( max_length=2000, null=True )
    date_added = models.DateTimeField( auto_now_add=True )
    user = models.ForeignKey( User, on_delete=models.CASCADE )

    def __str__(self):
        return f'{self.private_room} ({self.user})'
