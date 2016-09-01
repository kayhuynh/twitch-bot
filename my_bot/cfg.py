# Configurations for the bot

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "fpskhang" 	# Twitch username you made for the bot.
PASS = ""	# Password you got from twitchapps.tmi
CHAN = "dulangkhang"	# The username of the account you'll be streaming on.

# The IRC server only lets you send AT MOST 20 messages every 30 seconds
# Doing more would disconnect the bot.
RATE = (20/30)

# Dictionary of all users viewing the stream RIGHT NOW whose role is anything
# but the average viewer. 
# ie. Moderator.
op_list = {}