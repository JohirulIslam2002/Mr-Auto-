from telethon import TelegramClient, events

# তোমার তথ্যগুলো এখানে বসাও
api_id = 22543888        # উদাহরণ: 12345678
api_hash = 'b2c46c23f8d4d7defea5f97bd31be085'   # উদাহরণ: 'abcdef1234567890'
bot_token = '7901075451:AAFxnECgXc-OZmkymYxnPC_5L0bv6yrTUu0' # উদাহরণ: '1234567890:ABCDefGhIjkLmnoPQrstuvWXyz'

# চ্যানেল আইডি বা ইউজারনেম
source_channel = -1002650028621  # নোটিস করো: কোন কোটস নেই
target_channels = [-1002567599805, -1002622565716]  # লিস্ট আকারে, কোন কোটস নেই

# ক্লায়েন্ট তৈরি
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    for target in target_channels:
        try:
            await event.forward_to(target)
            print(f"Forwarded to {target}")
        except Exception as e:
            print(f"Failed to forward to {target}: {e}")

print("Bot is running...")
client.run_until_disconnected()
