 from twitchAPI.twitch import Twitch
 from os.path import exists
 from time import sleep
 
 client_id = 'YOUR CLIENT ID'
 client_secret = 'YOUR CLIENT SECRET'
 twitch = Twitch(client_id, client_secret)
 
channel_name = 'DESIRED CHANNEL'
channel_id = twitch.get_users(logins=[channel_name]).get('data')[0].get('id')
  
curr_follows = str(twitch.get_users_follows(first=1, to_id=channel_id)['total'])
  
while True:
    fp = open('count.txt', 'w')
    fp.write(curr_follows) 
    fp.close()
    print(f"Follow count updated [Followers: {curr_follows}]")
    sleep(30) # Updates every 30 seconds

