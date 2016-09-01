import string
from sock import send_message

def join_room(s):
	read_buffer = ""
	is_loading = True
	while is_loading:
		read_buffer = read_buffer + s.recv(1024)
		temp = string.split(read_buffer, "\n")
		read_buffer = temp.pop()
		for line in temp:
			print(line)
			is_loading = loading_complete(line)
	send_message(s, "Successfully joined chat")
	
def loading_complete(line):
	if("End of /NAMES list" in line):
		return False
	return True