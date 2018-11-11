# RPi_TCP_GPIO
A small example for a TCP-based communication over LAN to trigger GPIO pins on a Raspberry Pi

This small repository shows an example of how to trigger GPIO pins on a Raspberry Pi using TCP communication from within a LAN. The server-side script is meant to be run on a Raspberry Pi. The client-side script can be run from any device that can run Python, including Android devices using qpython. The supplied minimal API can be easily further extended to fit the needs of a given project.

To create this I borrowed some advice and sample code to build on from https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170 and the Socket Programming HOWTO on the python.org website.
