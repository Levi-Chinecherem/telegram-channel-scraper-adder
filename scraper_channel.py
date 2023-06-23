# (c) @Levi-Chinecherem
# Telegram: http://t.me/@SemanticDev
# Please give me credits if you use any codes from here.

from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch, InputPeerChannel
import csv

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = '+234 YOUR_PHONE_NUMBER'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print('Fetching Channels...')
channels = client.get_dialogs(limit=None, ignore_migrated=True, filter=lambda d: d.is_channel)

print('Choose a channel to scrape members from:')
for i, channel in enumerate(channels):
    print(f"{i}. {channel.title}")

channel_index = int(input("Enter a number: "))
target_channel = channels[channel_index]

print('Fetching Members...')
all_participants = []
channel = client.get_entity(target_channel.id)
for p in client.iter_participants(channel):
    all_participants.append(p)

print('Saving in file...')
csv_filename = f"{target_channel.title}_members.csv"
with open(csv_filename, "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'name', 'channel', 'channel id'])
    for user in all_participants:
        username = user.username if user.username else ""
        first_name = user.first_name if user.first_name else ""
        last_name = user.last_name if user.last_name else ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([username, user.id, user.access_hash, name, target_channel.title, target_channel.id])

print(f"Members scraped successfully. Saved to {csv_filename}.")
