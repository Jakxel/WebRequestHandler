from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


class WebRequestHandler(BaseHTTPRequestHandler):

    # Documentos almacenados en memoria
    
    contenido = {
        '/': """
<html>
  <h1>Home Page</h1>
  <ul>
    <li><a href="/proyecto/web-uno">Web Uno</a></li>
    <li><a href="/proyecto/web-dos">Web Dos</a></li>
    <li><a href="/proyecto/web-tres">Web Tres</a></li>
  </ul>
</html>
""",
        '/proyecto/web-uno': """
<html>
  <h1>Proyecto: web-uno</h1>
</html>
""",
        '/proyecto/web-dos': """
<html>
  <h1>Proyecto: web-dos</h1>
</html>
""",
        '/proyecto/web-tres': """
<html>
  <h1>Proyecto: web-tres</h1>
</html>
"""
    }

    def do_GET(self):
        ruta = urlparse(self.path).path

        if ruta in self.contenido:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.contenido[ruta].encode("utf-8"))
        else:
            self.send_error(404, "Page not found")


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()