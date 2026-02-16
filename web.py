from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        if self.valida_autor():
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(self.get_html().encode("utf-8"))
        else:
            self.send_error(404, "The author doesnt exist")

    def valida_autor(self):
        return 'autor' in self.query_data()
        
    def get_html(self):
        path_parts = self.url().path.strip("/").split("/")

        if len(path_parts) >= 2:
            proyecto = path_parts[1]
            autor = self.query_data()['autor']
            return f"<h1>Proyecto: {proyecto} Autor: {autor}</h1>"
        else:
            return "<h1>Invalid route</h1>"


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()