from telethon import TelegramClient

api_id = ''
api_hash = ''
phone = ''
password = ''

client = TelegramClient('session', api_id, api_hash)

async def get_chat_id():
    await client.start(phone=phone, password=password)
    async for dialog in client.iter_dialogs():
        print(f"Название: {dialog.name} | ID: {dialog.id} | Тип: {type(dialog.entity)}")

with client:
    client.loop.run_until_complete(get_chat_id())