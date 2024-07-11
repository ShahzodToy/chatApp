from django.urls import path
from a_rtchat.views import *

urlpatterns = [
    path('',chat_view,name='home'),
    path('chat/room/<chatroom_name>/',chat_view,name='chatroom'),
    path('chat/new-groupchat/',create_groupchat,name='new-groupchat'),
    path('chat/<username>/',get_or_create_chatroom,name='start-chat'),
]