# coding: utf-8

# third party
from anillo.handlers.routing import router as anillo_router, url

# guild empire back
import handlers


urls = [
    url("/api/v1/turn", handlers.get_turn, methods=["get"]),
    url("/api/v1/turn", handlers.post_turn, methods=["post"]),
]

router = anillo_router(urls)
