# Main code for bot to run

import config, utils
import utils
import socket
import re
import time, thread
from time import sleep


def main():
	s = socket.socket()
	s.connect((config.HOST, config.PORT))
	s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
	s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
	s.send("JOIN #{}\r\n".format(config.CHAN).encode("utf-8"))

	CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

	utils.chat(s, "Hey, all.") # What bot says when it joins the room.

	thread.start_new_thread(utils.thread_fill_op_list(), ())

	while True:
		resp = s.recv(1024).decode("utf-8")
		# Respond to IRC server with PONG to let the bot stay.
		if resp == "PING :tmi.twitch.tv\r\n":
			s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
		# Read the message 
		else:
			username = re.search(r"\w+", resp).group(0)
			message = CHAT_MSG.sub("", resp)
			print(resp)

			# Custom commands
			# ie. !time would give the time
			if message.strip() == "!time":
				utils.chat(s, "It is currently " + time.strftime("%I:%M %p %Z on %A, %B, %d, %Y.:))"))


		sleep(1)





if __name__ == "__main__":
	main()