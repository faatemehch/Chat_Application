from django.contrib import admin
from .models import Room, Message


class MessageAdmin( admin.ModelAdmin ):
    list_display = ['__str__', 'room']


admin.site.register( Room )
admin.site.register( Message, MessageAdmin )
