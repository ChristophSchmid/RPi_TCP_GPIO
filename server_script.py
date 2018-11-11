#!/usr/bin/env python3
"""
Server-side application for TCP-communication.
The server is a Raspberry Pi, the client can be
any device running Python, including Qpython
on Android devices.
"""

import socket
import tcp_gpio_api as tcp_gpio

# set up constants for TCP connection
HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

# create server socket
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind(ADDR)

# set up GPIOs using the custom API
tcp_gpio.setup_hardware()


if __name__ == '__main__':
    # start listening on the server
    SERVER.listen(5)
    print('Waiting for connection...')

    try:
        # infinite loop for connecting and replying to requests
        while True:
            # accept connections from outside
            (clientsocket, address) = SERVER.accept()

            # receive command from client
            received_msg = clientsocket.recv(BUFSIZ).decode('utf8')
            print('Server: received CMD ' + received_msg)
            # signal that socket won't receive anymore
            clientsocket.shutdown(socket.SHUT_RD)

            try:
                # call parser function to identify command string
                command = tcp_gpio.parse_cmd(received_msg)
            except NotImplementedError: # if command could not be identified
                # shut down socket with warnings
                print('WARNING: received command not implemented')
                clientsocket.shutdown(socket.SHUT_RD)
                clientsocket.send(bytes('Command not implemented: ' + received_msg, 'utf8'))
                clientsocket.shutdown(socket.SHUT_WR)
                clientsocket.close()
                continue

            # example for usage:
            # if command starts with 'LED', the according function
            # is called. This could be moved into a separate function.
            if command[0] == 'LED':
                tcp_gpio.toggle_led(command)

            # send confirmation and shut down the socket
            clientsocket.send(bytes('Command executed: ' + received_msg, 'utf8'))
            clientsocket.shutdown(socket.SHUT_WR)
            clientsocket.close()

    # if Ctrl-C is pressed, loop is closed and some clean-up is done
    except KeyboardInterrupt:
        SERVER.close()