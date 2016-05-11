from channels.routing import route

from .consumers import hello

channel_routing = [
    route('background-hello', hello),
]
