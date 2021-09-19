import socket
import json
import time
import sys

HOST, PORT = "localhost", 9999
# HOST, PORT = "192.168.0.232", 9999

DEFAULT_ENCODING = 'utf-8'


def sender(cmd, arg=None):

    tx_data = bytes(json.dumps(dict(cmd=cmd, arg=arg)), DEFAULT_ENCODING)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((HOST, PORT))
        sock.sendall(tx_data)
        received = str(sock.recv(8192), "utf-8")

        if received:
            data = json.loads(received)

        print("Sent:     {}".format(tx_data))
        print("Received: {}".format(received))
        print("Data:     {}".format(str(data)))

        return data or {}
