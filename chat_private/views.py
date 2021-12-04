from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from .models import PrivateRequest, PrivateChat


@login_required( login_url='account:login-user' )
def private_chat(request, user_1_id,user_2_id):
    user_1 = User.objects.filter( id=user_1_id ).first()
    user_2 = User.objects.filter( id=user_2_id ).first()
    look_up = (Q( user_1=user_1 ) & Q( user_2=user_2 ) | Q( user_1=user_2 ) & Q( user_2=user_1 ))
    private_chat_: PrivateChat = PrivateChat.objects.filter( look_up ).first()
    look_up = (Q( user_1=user_1 ) | Q( user_1=user_2 ))
    context = {
        'private_chat_': private_chat_,
        'contacts': PrivateChat.objects.filter( look_up ).distinct()
    }
    return render( request, 'chat_private/private_chat_page.html', context )


def send_request(request):
    user_1 = request.user  # request has been send from
    user_2 = request.POST['user_id']  # request has been send to
    PrivateRequest.objects.create( from_user=user_1, to_user=user_2 )
    return HttpResponse( 'your request has been send' )


def get_request(request):
    user_requests = PrivateRequest.objects.filter( to_user=request.user, is_accepted=False )
    context = {
        'requests': user_requests
    }
    return HttpResponse( 'you have a new request' )
