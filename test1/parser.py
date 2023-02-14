from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest

from settings import api_id, api_hash

with TelegramClient('name', api_id, api_hash) as client:
   # Get entity of channel
   channel = client.get_entity('https://t.me/market_marketplace')
   # Subscribe
   #client(JoinChannelRequest(channel))
   # Read
   count = 10
   for message in client.iter_messages(channel):
      print(message.sender_id, ':', message.text)
      if count == 0:
         break
      count -= 1
        

   client.run_until_disconnected()