import SimpleHTTPServer
import SocketServer

PORT = 3333

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("Joystick client can be found on", PORT)
httpd.serve_forever()