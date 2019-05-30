from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import board.routing


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            board.routing.websocket_urlpatterns
        )
    ),
})