import socket
import threading
import sys
import time
from random import randint


class Server:
    connections = []
    peers = []  # hosts join this network will be added in the peers list

    def __init__(self):
        # internet socket, TCP connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # when the server is disable, allow other hosts become a new server
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #  bound to host and port
        sock.bind(('0.0.0.0', 10000))
        sock.listen(1)
        print("Server running ...")
        while True:
            c, a = sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            self.peers.append(a[0])  # append the address of the peer
            print(str(a[0]) + ':' + str(a[1]), "connected")
            self.sendPeers()

    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                self.connections.remove(c)
                self.peers.remove(a[0])
                c.close()
                self.sendPeers()
                break

    def sendPeers(self):  # send the list of the peers to all host connect to the server
        p = ""
        for peer in self.peers:
            p = p + peer + ","

        for connection in self.connections:
            # \x11 use to differentiate the message and list of peers
            connection.send(b'\x11' + bytes(p, 'utf8'))


class Client:
    def sendMsg(self, sock):
        while True:
            sock.send(bytes(input(""), 'utf8'))

    def __init__(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((address, 10000))

        iThread = threading.Thread(target=self.sendMsg, args=(sock,))
        iThread.daemon = True
        iThread.start()

        while True:
            data = sock.recv(1024)
            if not data:
                break
            if data[0:1] == b'\x11':
                self.updatePeers(data[1:])
                print("got peers")
            else:
                print(str(data, 'utf-8'))

    def updatePeers(self, peerData):
        p2p.peers = str(peerData, "utf8").split(",")[:-1]


class p2p:
    peers = ['127.0.0.1']


while True:
    try:
        print("Trying to connect ...")
        # let every connector sleep for a random time
        time.sleep(randint(1, 3))
        for peer in p2p.peers:
            try:
                client = Client(peer)  # create a new client object
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                pass
            try:
                server = Server()  # every peer can try to become a server
            except KeyboardInterrupt:
                sys.exit(0)
            except:
                print("Couldn't start the server ...")
    except KeyboardInterrupt:
        sys.exit(0)
