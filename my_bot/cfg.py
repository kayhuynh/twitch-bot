# Configurations for the bot

HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "fpskhang"   # Twitch username you made for the bot.
PASS = "" # OAuth key from twitchapps.tmi
CHAN = "dulangkhang"    # The username of the streamer's chat to connect to.

# The IRC server only lets you send AT MOST 20 messages every 30 seconds
# Doing more would disconnect the bot.
RATE = (20/30)

# Dictionary of all users viewing the stream RIGHT NOW whose role is anything
# but the average viewer. 
# ie. Moderator.
op_list = {}