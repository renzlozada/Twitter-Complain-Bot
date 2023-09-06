import os
import time
from complaintBot import InternetSpeedXBot

complain_bot = InternetSpeedXBot()

complain_bot.get_internet_speed()

time.sleep(2)  # Adding a stop-gap or a breather
if complain_bot.down < 100 and complain_bot.up < 100:  # Checking if the Internet Speed is slow
    complain_bot.tweet_at_provider()
else:
    print("Internet speed is fine. No need to complain")
    exit()
