from django.contrib import admin
from .models import PrivateMessage, PrivateChat, PrivateRequest

admin.site.register( PrivateChat )
admin.site.register( PrivateMessage )
admin.site.register( PrivateRequest )
