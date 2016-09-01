# Utility functions to be used in bot.py
import cfg

import json
import urllib2
import time
import thread


def chat(sock, msg):
	"""Sends a message to the server connected to. 

	Params:
	sock -- socket used to send the message
	msg  -- the message to send
	""" 

	sock.send("PRIVMSG #{} :{}\r\n".format(cfg.CHAN, msg))


def ban(sock, user):
	"""Bans a user from the channel.

	Params:
		sock -- socket used to send ban command
		user -- user to be banned
	"""
	sock.send(chat(".ban {}".format(user)))


def timeout(sock, user, seconds=120):
	"""Timeout a user for a certain amount of time

	Params:
		sock 	-- socket used to send timeout command
		user 	-- user to be timed out
		seconds -- length of timeout in seconds
	"""
	chat(sock, ".timeout {}".format(user, seconds))


def thread_fill_op_list():
	"""Fill the op_list in cfg.py with information classifying
	each viewer in the chat and their role

	We must query twitch's chatters log (info about all the viewers
	for a particular streamer's channel), which returns a JSON formatted
	response, which we will use to fill our op_list.

	The response will look like:
		{
		  "_links": {},
		  "chatter_count": 0,
		  "chatters": {
		    "moderators": [],
		    "staff": [],
		    "admins": [],
		    "global_mods": [],
		    "viewers": []
		  }
		}
	"""
	while True:
		try:
			url = "http://tmi.twitch.tv/group/user/{}/chatters".format(cfg.CHAN)
			req = urllib2.Request(url, headers={"accept": "*/*"})
			resp = urllib2.urlopen(req).read()
			if resp.find("502 Bad Gateway") == -1:	# Sometimes we can't connect
				cfg.op_list.clear()
				data = json.loads(resp)
				chatters = data["chatters"]
				for key in chatters["moderators"]:
					cfg.op_list[key] = "mod"
				for key in chatters["staff"]:
					cfg.op_list[key] = "staff"
				for key in chatters["admins"]:
					cfg.op_list[key] = "admin"
				for key in chatters["global_mods"]:
					cfg.op_list[key] = "global_mod"
		except:
			pass

		time.sleep(3)


def is_op(user):
	""" If the user is a moderator, mod, staff, admin or global mod,
	this function returns true
	"""
	return user in cfg.op_list

