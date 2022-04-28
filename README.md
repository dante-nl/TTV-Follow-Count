# Twitch-Follow-Count
Script that uses Python and twitchAPI to write a Twitch Channel's current follower count to a text file. Primarily made for a simple follower counter in OBS.

## Prerequisites
- **Python** installed and running on your system
- **twitchAPI** for Python; install [online](https://pypi.org/project/twitchAPI/) or with pip:
>```pip install twitchAPI```
- Go to [Twitch's Dev Console](https://dev.twitch.tv/console/apps) and register an application.
> Make sure to use ```https://localhost:17563``` as your redirect link. Press **Create Secret** and **Save** as well. Jot down your client ID and secret for the initial setup (see below)

## Initial Setup

After aquiring **tracker.py** and moving it to your desired directory, edit the file with any text/code editor of choice. This is where you'll need your Client ID and secret; there a few things to change:
- Replace ```YOUR CLIENT ID``` and ```YOUR CLIENT SECRET``` with the corresponding values given when registering the app with Twitch's Dev Console, (Lines 4 and 5)
- Replace ```DESIRED CHANNEL``` with the name of the channel you'd like to track (Line 8)

## Usage

Simply run the script and presto! The follower count of that channel should be written in the text file **tracker_count.txt** every 30 seconds!
