from django.shortcuts import render
# Create your views here.
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#      {'id': 3, 'name': 'front end developer'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)
