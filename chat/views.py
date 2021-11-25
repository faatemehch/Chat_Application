from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .models import Room, Message
from django.http import JsonResponse
from django.forms.models import model_to_dict


def home_view(request):
    context = {'title': 'Chat Application'}
    return render( request, 'chat/home_view.html', context )


@login_required
def room(request, room_name):
    print( 'room_name', room_name )
    room = Room.objects.get( room_name=room_name )
    messages = room.message_set.all()
    context = {
        'title': f'Chat App | {room.room_name}',
        'room': room,
        'messages': messages,
        'username': request.user.username

    }
    return render( request, 'chat/chat-room.html', context )


@login_required
def check_room(request):
    room_name = request.POST['room_name']
    if request.method == 'POST':
        room = Room.objects.filter( room_name=request.POST['room_name'] ).first()
        if room is None:
            room = Room.objects.create( room_name=request.POST['room_name'] )
            room.save()
        # return redirect( 'chat:room', room_name=room_name, username=request.user.username )
        return redirect( '/' + room_name + '/?username=' + request.user.username )
    return redirect( 'chat:home-view' )


def send_message(request):
    if request.is_ajax():
        form_data, room_name = request.GET.get( ['form_data'][0] ), request.GET.get(
            ['room_name'][0] )  # data from send form
        room = Room.objects.get( room_name=room_name )
        new_message = Message.objects.create( owner=request.user, message_text=form_data, room=room )
        print( new_message.owner )
        return HttpResponse( 'Message Sent Successfully' )
        # return JsonResponse( {'message': model_to_dict( new_message )} )


def get_messages(request, room_name):
    room = Room.objects.filter( room_name=room_name ).first()
    messages = room.message_set.all()
    username = []
    pull = []
    for msg in messages:
        if request.user.username == msg.owner.username:
            pull.append( 'right' )
        else:
            pull.append( 'left' )
        username.append( msg.owner.username )
    context = {
        'messages': list( messages.values() ),
        'user_name': username,
        'pulls': pull
    }
    return JsonResponse( context )
