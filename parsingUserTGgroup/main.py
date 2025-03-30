from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import *
import pandas as pd
api_id = ''
api_hash = ''
phone = ''
password = ''
chat_username = ''

client = TelegramClient('session', api_id, api_hash)


async def main():
    try:
        print("Начинаем авторизацию...")
        await client.start(phone=phone, password=password)
        print("Авторизация успешна!")

        print("Получаем информацию о чате...")
        chat = await client.get_entity(chat_username)
        print(f"Чат найден: {chat.title}")

        print("Собираем участников...")
        participants = await client.get_participants(chat, aggressive=True)
        print(f"Собрано {len(participants)} участников.")

        data = []
        for user in participants:
            # Используем GetFullUserRequest для получения полного описания
            full_user = await client(GetFullUserRequest(user))
            user_about = getattr(full_user.full_user, 'about', '—')
            print(full_user)

            data.append({
                'Никнейм': user.username or '—',
                'Описание': user_about,
                'Premium': '+' if getattr(user, 'premium', False) else '-'
            })

        df = pd.DataFrame(data)
        df.to_excel('members.xlsx', index=False)
        print("Данные сохранены в members.xlsx")

    except FloodWaitError as e:
        print(f"Ошибка: Заблокировано на {e.seconds} секунд.")
    except ChannelPrivateError:
        print("Ошибка: Чат приватный.")
    except UsernameInvalidError:
        print("Ошибка: Неверный username.")
    except AuthKeyUnregisteredError:
        print("Ошибка: Сессия не зарегистрирована. Удалите файл session.session.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


with client:
    client.loop.run_until_complete(main())
