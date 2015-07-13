import os.path

from anillo.handlers.routing import router as anillo_router, url

import handlers

urls = [
    url("/api/v1/test", handlers.test, methods=["get"]),
]

router = anillo_router(urls)

