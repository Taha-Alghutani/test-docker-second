from django.shortcuts import render
import socket

# Create your views here.
def index(request):
    hostname = socket.gethostname()
    return render(request, 'app/index.html', {
        'container_id': hostname
    })
