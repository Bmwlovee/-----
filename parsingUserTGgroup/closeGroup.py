from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
import pandas as pd

api_id = ''
api_hash = ''
phone = ''
password = ''
chat_id = -11111

client = TelegramClient('session', api_id, api_hash)


async def main():
    await client.start(phone=phone, password=password)
    chat = await client.get_entity(chat_id)
    participants = await client.get_participants(chat, aggressive=True)

    data = []
    for user in participants:
        full_user = await client(GetFullUserRequest(user))
        user_about = getattr(full_user.full_user, 'about', '—')

        data.append({
            'Никнейм': user.username or '—',
            'Описание': user_about,
            'Premium': '+' if getattr(user, 'premium', False) else '-'
        })

    df = pd.DataFrame(data)
    df.to_excel('members2.xlsx', index=False)
    print("Данные сохранены в members2.xlsx")


with client:
    client.loop.run_until_complete(main())