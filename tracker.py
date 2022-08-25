from twitchAPI.twitch import Twitch
from time import sleep
from datetime import datetime

### ⬇️ ENTER YOUR INFO HERE ⬇️ ###
client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'
channel_name = 'DESIRED CHANNEL'

twitch = Twitch(client_id, client_secret)
channel_id = twitch.get_users(logins=[channel_name]).get('data')[0].get('id')

last_follows = 0

while True:
    curr_follows = str(twitch.get_users_follows(first=1, to_id=channel_id)['total'])
    
    # Update only if follow count has changed
    if (curr_follows != last_follows):
        last_follows = curr_follows
        curr_time = datetime.now().strftime("%H:%M:%S")
        
        fp = open('count.txt', 'w')
        fp.write(curr_follows) 
        fp.close()
        
        print(f"[{curr_time}]: Follow count updated to {curr_follows}")
        
    sleep(30) # Updates every 30 seconds
