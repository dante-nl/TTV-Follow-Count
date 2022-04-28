  1 from twitchAPI.twitch import Twitch
  2 from os.path import exists
    from time import sleep
  3 
  4 client_id = 'YOUR CLIENT ID'
  5 client_secret = 'YOUR CLIENT SECRET'
  6 twitch = Twitch(client_id, client_secret)
  7 
  8 channel_name = 'DESIRED CHANNEL'
  9 channel_id = twitch.get_users(logins=[channel_name]).get('data')[0].get('id')
 10 
 11 curr_follows = str(twitch.get_users_follows(first=1, to_id=channel_id)['total'])
 12 
 4 while True:
 15     fp = open('count.txt', 'w')
 16     fp.write(curr_follows) 
 17     fp.close()
 18     print(f"Follow count updated [Followers: {curr_follows}]")
 19     time.sleep(30) # Updates every 30 seconds

