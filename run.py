import string
from read import get_user, get_message
from sock import open_socket, send_message
from init import join_room

s = open_socket()
join_room(s)
read_buffer = ""

while True:
	read_buffer = read_buffer + s.recv(1024)
	temp = string.split(read_buffer, "\n")
	read_buffer = temp.pop()
	
	for line in temp:
		print(line)
		if "PING" in line:
			s.send(line.replace("PING", "PONG"))
			break
		user = get_user(line)
		message = get_message(line)
		print user + " typed :" + message
		if "You Suck" in message:
			send_message(s, "No, you suck!")
			break
