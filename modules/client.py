import socket
import json

# HOST, PORT = "localhost", 9999
HOST, PORT = "192.168.0.232", 9999
DEFAULT_ENCODING = 'utf-8'

def make_vlc(cmd, arg=None):

    return bytes(json.dumps(dict(cmd=cmd, arg=arg)), DEFAULT_ENCODING)


def sender(tx_data):

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        sock.connect((HOST, PORT))
        sock.sendall(tx_data)

        received = str(sock.recv(1024), "utf-8")
        data = json.loads(received)

        # print("Sent:     {}".format(data))
        print("Received: {}".format(received))

    return data



if __name__ == '__main__':
    vlc = make_vlc('get_status')
    print(vlc)
    sender(vlc)
    vlc = make_vlc('set_path', '/home/Music/')
    print(vlc)
    sender(vlc)


"""
Received: {"cmd": "get_status", "arg": null, "status": "idle"}
Received: {"cmd": "get_status", "arg": null, "status": "State.NothingSpecial"}

"""
