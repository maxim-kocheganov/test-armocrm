from telethon.sync import TelegramClient

from .settings import api_id, api_hash

def getPostsFromTG(channelInText):
   posts = []
   with TelegramClient('dev', api_id, api_hash) as client:      
      # Get entity of channel
      channel = client.get_entity(channelInText)
      count = 10
      for message in client.iter_messages(channel):
         # print(message.sender_id, ':', message.text)
         posts.append({'channel':channelInText, 'text':message.text})
         if count == 0:
            break
         count -= 1
   return posts

if __name__ == "__main__":
   with TelegramClient('dev', api_id, api_hash) as client: # Login from console
      pass