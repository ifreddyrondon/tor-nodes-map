from django.shortcuts import render
from models import Node


def map_nodes(request):
    nodes = Node.objects.all().values('ip', 'latitude', 'longitude')

    return render(request, 'tor/map_nodes.html', {
        "markers": list(nodes)
    })
