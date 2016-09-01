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


	utils.chat(s, "Hey, all.") # What bot says when it joins the room.




if __name__ == "__main__":
	main()