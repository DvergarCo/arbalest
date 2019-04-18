from websocket_server import WebsocketServer
import threading
import time

client_count = 0
robots = []
running = False


def get_server_status():
    return running

def new_client(client, server):
    print("New connection")


def client_left(client, server):
    print("Lost connection")


def message_received(client, server, message):
    global robots

    if (message == "NEW ROBOT"):
        print("NEW ROBOT REGISTERED")
        robots.append(client)
    else:
        # message structure "[RobotIndex]:[OTHER]"
        parts = message.split(":")
        robotId = int(parts[0])
        server.send_message(robots[robotId], parts[1])


if __name__ == "__main__":
    port = 9000
    print("Creating websocket server on port %d..." % port)
    server = WebsocketServer(port)
    server.set_fn_new_client(new_client)
    server.set_fn_client_left(client_left)
    server.set_fn_message_received(message_received)
    print("Server is running on port %d!" % port)
    running = True
    server.run_forever()
