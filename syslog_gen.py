#!/usr/bin/env python3
'''
Syslog Generator

Had a need to generate generic syslog messages to 
test open source logging solutions.
'''

import socket
import argparse
import random

def syslog_sender(message, host, port):
	try:
	    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    message = bytes(message, 'UTF-8')
	    send = sock.sendto(message, (host, port))
	finally:
		sock.close()




if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("--host", required=True,
						help="Remote host to send messages")
	parser.add_argument("--port", type=int, required=True,
						help="Remote port to send messages")
	parser.add_argument("--file", required=True, 
						help="Read messages from file")
	parser.add_argument("--count", type=int, required=True,
						help="Number of messages to send")
	parser.add_argument("--batch", help="Use with count flag to send \
		                X messages in X interval, batch being interval")
	
	args = parser.parse_args()
		(args.host, args.port))
	
	try:
		with open(args.file, 'r') as sample_log:
			random_logs = random.sample(list(sample_log), args.count)
	except FileNotFoundError:
		print("Please specify valid file name")
		exit(1)

	print("[+] Sending {0} messages to {1} on port {2}".format
				(args.count, args.host, args.port))
	for message in random_logs:
		syslog_sender(message, args.host, args.port)


'''
TODO:

Need to have options for burst that requires delay
'''