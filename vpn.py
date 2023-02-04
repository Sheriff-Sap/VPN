import socket
import selectors

class VPN:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.selector = selectors.DefaultSelector()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        print("VPN listening on", (self.host, self.port))
        self.selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=self.accept_connection)

    def accept_connection(self, server_socket):
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from", client_address)
        self.selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=self.receive_data)

    def receive_data(self, client_socket):
        data = client_socket.recv(1024)
        if data:
            print("Received data:", data)
            client_socket.sendall(data)
        else:
            self.selector.unregister(client_socket)
            client_socket.close()

    def run(self):
        while True:
            events = self.selector.select()
            for key, event in events:
                callback = key.data
                callback(key.fileobj)

if __name__ == "__main__":
    vpn = VPN("127.0.0.1", 8080)
    vpn.start()
    vpn.run()
