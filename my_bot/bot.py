# Main code for bot to run

import cfg, utils
import utils
import socket
import re
import time
from threading import Thread



def connect_to_chat(sock, streamer, bot_name, bot_pass):
	sock.connect((cfg.HOST, cfg.PORT))
	sock.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
	sock.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
	sock.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))


def main():
	s = socket.socket()
	connect_to_chat(s, cfg.CHAN, cfg.NICK, cfg.PASS)

	CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

	utils.chat(s, "Hey, all.") # What bot says when it joins the room.

	# Start new thread so bot updates op_list every specified amount of seconds.
	thread = Thread(target=utils.thread_fill_op_list, args=())
	thread.start()

	while True:
		resp = s.recv(1024).decode("utf-8")
		# Respond to IRC server with PONG to let the bot stay in chat.
		if resp == "PING :tmi.twitch.tv\r\n":
			s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
		else:
			username = re.search(r"\w+", resp).group(0)
			message = CHAT_MSG.sub("", resp)
			print(resp)

			# Custom commands
			# ie. !time would give the time
			if message.strip() == "!time":
				utils.chat(s, "It is currently " + time.strftime("%I:%M %p %Z on %A, %B, %d, %Y."))


		time.sleep(1)

	utils.chat(s, "Bye, Felicia")





if __name__ == "__main__":
	main()