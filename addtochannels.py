import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import time
import asyncio
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
"""
Adds one or more users to one or more channels (or megagroups). Managed entirely with plain text files by default.
"""

# This script requires Python 3 and Telethon, not sure about the minimum python version. I'm using 3.7.
# Change this if you wish to store these values somewhere else. Default locations, format, and mini-guide:
# Get the API key and API hash (for this script to be able to access Telegram in your behalf) by creating an application in my.telegram.org. Put them in a file called api.txt, each in one line, in that order.
# Put the channel names in channels.txt, one per line.
# Put the aliases in aliases.txt, one per line.

with open('api.txt', 'r', encoding = 'utf-8') as f:
    values = f.read().splitlines()
    api_id = int(values[0])
    api_hash = values[1]
with open('aliases.txt', 'r', encoding = 'utf-8') as f:
    users = f.read().splitlines()
with open ('channels.txt', 'r', encoding = 'utf-8') as f:
    channels = f.read().splitlines()

async def add_to_channels(channels: list, users: list):
    """
    Invites the users to the channels or megagroups. Both are lists. The members of these lists can be the actual names of the users and channels.
    """
    cached_channels = []
    for channel in channels:
        try:
            cached_channels.append(await client.get_input_entity(channel))
        except ValueError :
            dialogs = await client.get_dialogs()
            cached_channels.append(await client.get_input_entity(channel))
        for alias in aliases:
            print(alias)
            for channel in cached_channels:
                await client(InviteToChannelRequest(channel, [alias]))
                time.sleep(10) # Maybe not necessary, but I don't want to get flood protection.
            print("Done")
            time.sleep(10) # See comment above.

async def main():
    async with await TelegramClient('tsession', api_id, api_hash).start() as client:
        await add_to_channels(channels = channels, users = users)
asyncio.run(main())
