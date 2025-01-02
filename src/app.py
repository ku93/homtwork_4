from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        if self.path.startswith('/static/'):
            self.handle_static_files()
        else:
            self.send_html_file("../catalog/templates/contacts.html")

    def handle_static_files(self):
        """ Обслуживание статических файлов """
        file_path = f"..{self.path}"
        if os.path.exists(file_path):
            self.send_response(200)
            self.send_header("Content-type", self.get_content_type(file_path))
            self.end_headers()
            with open(file_path, "rb") as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def get_content_type(self, file_path):
        """ Возвращает корректный Content-Type для файла """
        if file_path.endswith(".css"):
            return "text/css"
        elif file_path.endswith(".js"):
            return "application/javascript"
        elif file_path.endswith(".svg"):
            return "image/svg+xml"
        elif file_path.endswith(".ico"):
            return "image/x-icon"
        else:
            return "application/octet-stream"

    def send_html_file(self, file_path):
        """ Обслуживание HTML-файлов """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                html_content = file.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html_content, "utf-8"))
        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
