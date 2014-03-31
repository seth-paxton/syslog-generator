#!/usr/bin/env python3
'''
Syslog Generator

Had a need to generate generic syslog messages to 
test open source logging solutions.
'''

import socket
import argparse

def syslog_sender(message, host, port):
	try:
	    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    message = bytes(message, 'UTF-8')
	    send = sock.sendto(message, (host, port))
	finally:
		sock.close()

def help_menu():
	parser = argparse.ArgumentParser()
	parser.parse_args()


if __name__ == "__main__":

	#message = "Syslog Generator Test"
	#host = "10.211.55.15"
	#port = 514

	parser = argparse.ArgumentParser()
	parser.add_argument("--host", required=True,
						help="Remote host to send messages")
	parser.add_argument("--port", type=int, required=True,
						help="Remote port to send messages")
	parser.add_argument("--file", required=True, 
						help="Read messages from file")
	parser.add_argument("--count", help="Number of messages to send")
	args = parser.parse_args()
	
	if args.count:
		print("[+] Sending {0} messages to {1} on port {2}".format
				(args.count, args.host, args.port))
		syslog_sender(args.file, args.host, args.port)
	else:
		print("[+] Sending messages to {0} on port {1}".format
				(args.host, args.port))

'''
TODO:

Should also randomize what gets picked from the file. Do not send message sequentially. 
Need to create function to read random lines from file. 
Need a while statement that will do the counting
'''