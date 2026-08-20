from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent

# Render fornece a porta através da variável PORT
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8000"))


class AgroLinkHandler(SimpleHTTPRequestHandler):
    """Serve os arquivos estáticos do AgroLink."""

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            directory=str(PROJECT_ROOT),
            **kwargs
        )

    def log_message(self, format_string, *args):
        print(
            f"[{self.log_date_time_string()}] "
            f"{format_string % args}"
        )


if __name__ == "__main__":
    server = ThreadingHTTPServer(
        (HOST, PORT),
        AgroLinkHandler
    )

    print(f"AgroLink iniciado em 0.0.0.0:{PORT}")
    print(f"Porta utilizada: {PORT}")

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nServidor encerrado.")

    finally:
        server.server_close()