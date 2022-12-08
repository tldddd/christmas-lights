from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socketserver

from app import App

# open json file and give it to data variable as a dictionary
# with open("db.json") as data_file:
#   data = json.load(data_file)

# Defining a HTTP request Handler class
class ServiceHandler(BaseHTTPRequestHandler):
    def __init__(
        self,
        request: bytes,
        client_address: tuple[str, int],
        server: socketserver.BaseServer,
    ) -> None:
        self.app: App = App()

        super().__init__(request, client_address, server)

    # sets basic headers for the server
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        # reads the length of the Headers
        length = int(self.headers["Content-Length"])
        # reads the contents of the request
        content = self.rfile.read(length)
        temp = str(content).strip("b'")
        self.end_headers()
        return temp

    # GET Method Defination
    def do_GET(self):
        # defining all the headers
        print(f"in_get, number is {self.test}")
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

    # prints all the keys and values of the json file
    # self.wfile.write(json.dumps(data).encode())

    ########
    # CREATE#
    ########
    # POST method defination
    def do_POST(self):
        print("in_post")

        # Read the JSON
        content_len = int(self.headers.get("Content-Length"))
        post_body = self.rfile.read(content_len)

        # Read the body.

        self.app

        return
        temp = self._set_headers()
        key = 0
        # getting key and value of the data dictionary
        for key, value in data.items():
            pass
        index = int(key) + 1
        data[str(index)] = str(temp)
        # write the changes to the json file
        with open("db.json", "w+") as file_data:
            json.dump(data, file_data)
        # self.wfile.write(json.dumps(data[str(index)]).encode())


# Server Initialization
print("Create server")
server = HTTPServer(("127.0.0.1", 8080), ServiceHandler)
server.serve_forever()
