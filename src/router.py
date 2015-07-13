import os.path

from anillo.handlers.routing import router as anillo_router, url

import handlers

urls = [
    url("/api/v1/turn", handlers.get_turn, methods=["get"]),
]

router = anillo_router(urls)
