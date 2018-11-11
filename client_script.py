#!/usr/bin/env python3
"""
Client-side application for TCP-communication.
The server is a Raspberry Pi, the client can be
any device running Python, including Qpython
on Android devices.
"""

import socket

# list of possible commands
cmdlist = ['LED_1_ON',
           'LED_2_ON',
           'LED_3_ON',
           'LED_1_OFF',
           'LED_2_OFF',
           'LED_3_OFF'
           ]

try:
    # infinite loop for receiving user choice
    while True:
        cmd = input("Select command to send:\n" +
                    "1) LED 1 on\n" +
                    "2) LED 2 on\n" +
                    "3) LED 3 on\n" +
                    "4) LED 1 off\n" +
                    "5) LED 2 off\n" +
                    "6) LED 3 off\n" +
                    "q) quit program\n")
        # check and handle input
        if not cmd.isnumeric():
            if cmd.lower() == 'q':
                break
            else:
                print("Command unknown\n\n")
                continue
        elif int(cmd) not in [1,2,3,4,5,6]:
            print("Command unknown\n\n")
            continue

        # create an INET, STREAMing socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to the RPi server
        client.connect(("192.168.178.31", 33000)) # IP and port can be chosen as needed

        # transmit the requested command to server
        client.send(bytes(cmdlist[int(cmd) - 1], "utf8"))
        client.shutdown(socket.SHUT_WR)

        # print out server response
        print(client.recv(1024).decode("utf8"))

        # close socket and wait for new input
        client.close()

# interrupt loop by Ctrl-C and clean up
except KeyboardInterrupt:
    if 'client' in locals():
        client.close()
