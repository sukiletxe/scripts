# This scripts requires Python 3 and Telethon, not sure about the minimum python version. I'm using 3.7.
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

async def add_to_channels(channels: list, users: list):
    """
    Invites the users to the channels or megagroups. Both are lists. The members of these lists can be the actual name of the users and channels. Note that supergroups are considered channels.
    """
    cached_channels = []
    for channel in channels:
        cached_channels.append(await client.get_input_entity(channel))
        for alias in aliases:
            print(alias)
            for channel in cached_channels:
                await client(InviteToChannelRequest(channel, [alias]))
                time.sleep(10)
            print("hecho")
            time.sleep(10)


# Change this if you wish to store these values somewhere else
with open('api.txt', 'r') as f:
    values = f.read().splitlines()
    api_id = int(values[0])
    api_hash = values[1]
with open('aliases.txt', 'r') as f:
    aliases = f.read().splitlines()
with open ('channels.txt', 'r') as f:
    channels = f.read().splitlines()

with TelegramClient('tsession', api_id, api_hash) as client:
    client.loop.run_until_complete(add_to_channels(channels = channels, users = aliases))