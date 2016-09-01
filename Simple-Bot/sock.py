import socket
from config import *

def open_socket():
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + IDENT + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s
	
def send_message(s, message):
	message_temp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send(message_temp + "\r\n")
	print("Sent: " + message_temp)