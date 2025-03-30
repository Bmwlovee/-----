# Парсер пользователей Телеграмм Групп    
После выполнения возвращает excel таблицу со столбцами: Username, описание, Telegram-Premium(+/-).
В файлах так же имеется GetChatId: получение id всех бесед на акканте, и файл CloseGroup, предназначенный для парсинга закрытых групп.
## Как использовать?
Необходимо зарегестрироваться на https://telegram.org/apps. Создать приложение и взять оттуда параметры: api_id, api_hash и вставить их в соответствующие поля в скрипте. Так же необходимо ввести номер телефона и пароль от аккаунта(если имеется). 
## Если чат открытый
В поле chat_username необходимо ввести username чата, копиурем ссылку чата. Например: https://t.me/abrakadabra000001. username чата будет: abrakadabra000001. Дальше запускаем скрипт, и в корневой папке проекта будет файл members.xlsx
## Если чат закрытый
Сначала открываем скрипт GetChatId, вводим все необходимые данные, запускаем скрипт. В списке ищем необходимый чат, берем его ID. Переходим в скрипт CloseGroup, в поле chat_id вставляем этот ID. (Обязательно с минусом в начале!). Запускаем скрипт, получаем на выходе в корневой папке проекта файл members2.xlsx
