# Main code for bot to run

import cfg, utils
import utils
import socket
import re
import time
from threading import Thread


def connect_to_chat(sock):
    """Connects to a streamer's chat using Twitch IRC. 
       Credentials for the bot go here.

    Params: 
    sock -- socket used to connect to stream.
    streamer -- the streamer's chat you want to connect to.
    bot_name -- The username you created on Twitch.tv that will 
                be used for the bot in lowercase.
    bot_pass -- password for bot in in lowercase.
    """
    sock.connect((cfg.HOST, cfg.PORT))
    sock.send("PASS {}\r\n".format(cfg.PASS))
    sock.send("NICK {}\r\n".format(cfg.NICK))
    sock.send("JOIN #{}\r\n".format(cfg.CHAN))


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect_to_chat(s)

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

    utils.chat(s, "Hey, all.") # What bot says when it joins the room.

    # Start new thread so bot updates op_list every specified amount of seconds.
    thread = Thread(target=utils.thread_fill_op_list, args=())
    thread.start()

    while True:
        resp = s.recv(1024).decode("utf-8")
        # Respond to the server with PONG to let the bot stay in chat.
        if resp is None:
            break
        if resp == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", resp).group(0)
            message = CHAT_MSG.sub("", resp)
            print(resp)

            # Custom commands
            # ie. !time would give the time
            msg = message.strip()
            if msg == "!time":
                utils.chat(s, "It is currently " + time.strftime("%I:%M %p %Z on %A, %B, %d, %Y."))

        time.sleep(1)




if __name__ == "__main__":
    main()