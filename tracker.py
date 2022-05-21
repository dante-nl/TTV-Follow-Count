from twitchAPI.twitch import Twitch
from time import time, sleep
from datetime import timedelta

client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'
channel_name = 'DESIRED CHANNEL'

twitch = Twitch(client_id, client_secret)
channel_id = twitch.get_users(logins=[channel_name]).get('data')[0].get('id')

start = time()

while True:
    time_elapsed = int(time() - start)
    curr_follows = str(twitch.get_users_follows(first=1, to_id=channel_id)['total'])
   
    fp = open('count.txt', 'w')
    fp.write(curr_follows) 
    fp.close()
    
    print(f"[{timedelta(seconds = time_elapsed)}]: Follow count updated to {curr_follows}")
    sleep(30) # Updates every 30 seconds
