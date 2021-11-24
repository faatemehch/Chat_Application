from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Message


def home_view(request):
    context = {'title': 'Chat Application'}
    return render( request, 'chat/home_view.html', context )


@login_required
def room(request, room_name, username):
    room = Room.objects.get( room_name=room_name )
    context = {
        'title': f'Chat App | {room.room_name}',
        'room': room,

    }
    return render( request, 'chat/chat-room.html', context )


@login_required
def check_room(request):
    room_name = request.POST['room_name']
    username = request.POST['username']
    if request.method == 'POST':
        room = Room.objects.filter( room_name=request.POST['room_name'] ).first()
        if room is None:
            room = Room.objects.create( room_name=request.POST['room_name'] )
            room.save()
        return redirect( 'chat:room', room_name=room_name, username=username )

    return redirect( 'chat:home-view' )
