# VPN
# Documentation for VPN

This VPN is a simple implementation of a virtual private network in Python. It uses the `socket` module to create a server socket and listen for incoming connections from clients. The `selectors` module is used to efficiently handle multiple connections in a non-blocking manner

# Class Definition
The VPN class is defined as follows:

![1](https://user-images.githubusercontent.com/103308810/216769686-c5b60b82-4469-4a1e-9541-b2e8cc9c6fca.PNG)

The class takes the `host` and `port` as arguments and initializes them as instance variables. The `selector` is initialized using the `DefaultSelector` class from the `selectors` module.

# Method Descriptions
`start` method

![2](https://user-images.githubusercontent.com/103308810/216769921-c7136665-7d96-4e5f-bc20-29de0f0abe7d.PNG)

The `start` method creates a server socket using the `socket` module and binds it to the specified `host` and `port`. It then listens for incoming connections and prints a message indicating that the VPN is listening. Finally, it registers the server socket with the selector using the `register` method, specifying the `accept_connection` method as the callback to be invoked when there is a `EVENT_READ` event on the socket.

# `accept_connection` method

![3](https://user-images.githubusercontent.com/103308810/216770074-5b310056-619b-4867-abec-306e34376b65.PNG)

The `accept_connection` method is called when there is a `EVENT_READ` event on the server socket. It accepts the incoming connection and prints a message indicating the client address. It then registers the client socket with the selector using the `register` method, specifying the `receive_data` method as the callback to be invoked when there is a `EVENT_READ` event on the socket.

# `receive_data` method

![4](https://user-images.githubusercontent.com/103308810/216770239-427796fb-45a9-4971-8aa1-75e00a63a086.PNG)

The `receive_data` method is called when there is a `EVENT_READ event` on a client socket. It receives data from the client using the `recv` method, and if the data is not empty, it prints the received data and sends it back to the client using the `sendall` method. If the data is empty, it unregisters the client socket with the selector and closes it.

# `run` method

![5](https://user-images.githubusercontent.com/103308810/216770427-4ce11a21-15ad-4085-8d47-6c3b99695798.PNG)

The `run` method in the above code is the main event loop of the VPN. It runs an infinite loop that waits for events to occur and then processes them. The `selector.select` method is used to wait for events, and the `key.data` attribute is used to get the callback function to be called for each event. The callback function is then called with the `key.fileobj` attribute, which is the file object associated with the event. This process is repeated for each event in the `events` list until the program is terminated. The run method is responsible for managing the network connections and handling the incoming and outgoing data.

# `if __name__ == "__main__":` block

![6](https://user-images.githubusercontent.com/103308810/216770701-18bb77c7-ee4b-4d2a-9c08-aa3343c60c89.PNG)

This code block is the main function that creates an instance of the VPN class and starts the VPN server. The `if __name__ == "__main__"` line ensures that this block is only executed when the script is run as the main program, not when it is imported as a module. The line `vpn = VPN("127.0.0.1", 8080)` creates an instance of the VPN class, with the host set to "127.0.0.1" (localhost) and the port set to 8080. The line `vpn.start()` starts the VPN server by binding the socket to the specified host and port and registering it with the selector for incoming connections. Finally, the line `vpn.run()` runs the VPN server by continuously selecting for incoming events, accepting connections, and receiving data from clients.

