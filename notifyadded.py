import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon.sync import TelegramClient
from telethon import events
from telethon.tl.functions.messages import GetCommonChatsRequest
from telethon.tl.types import UserEmpty
import asyncio
# This script requires Python 3 and Telethon, not sure about the minimum python version. I'm using 3.9.
# Change this if you wish to store these values somewhere else. Default locations, format, and mini-guide:
# Get the API key and API hash (for this script to be able to access Telegram in your behalf) by creating an application in my.telegram.org. Put them in a file called api.txt, each in one line, in that order.
# Simply run this. The groups you get added to (when this is running and between runs) will be notified to saved messages. Note that the between runs part doesn't work that well as of now, you may want it to run permanently.
with open('api.txt', 'r', encoding = 'utf-8') as f:
    values = f.read().splitlines()
    api_id = int(values[0])
    api_hash = values[1]

# Taken from https://github.com/LonamiWebs/Telethon/issues/1534
async def wait_catch_up(client):
    await client.catch_up()
    while client._updates_queue:
        await asyncio.wait(client._updates_queue, return_when=asyncio.ALL_COMPLETED)


async def handler(event):
    me = await client.get_me()
    group = await event.get_chat()
    by = await event.get_added_by()
    if by is not None and me in event.users:
        if isinstance(by, UserEmpty):
            msg = f"A user with ID {by.id} has added you to {group.title}"
        else:
            name = "{} {}".format(by.first_name, by.last_name or "").strip()
            nouser = "No username"
            username = f"[@{by.username}](@{by.username})" if by.username else nouser
            msg = f"{name} ({username}) has added you to {group.title}."
        common_groups = await client(GetCommonChatsRequest(by, limit = 0, max_id = 0))
        common_groups = common_groups.chats
        common_groups.remove(group)
        if common_groups:
            common_titles = [x.title for x in common_groups]
            msg += "\nYou both have the following groups in common:\n"
            msg += '\n'.join(common_titles)
        await client.send_message(me.id, msg)
        await client(MarkDialogUnreadRequest(peer = me, unread = True))

async def main():
    client.add_event_handler(handler, events.ChatAction)
    await wait_catch_up(client)
    await client.run_until_disconnected()
with TelegramClient('tsession', api_id, api_hash) as client:
    client.loop.run_until_complete(main())

