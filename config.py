import os

#Токен для обнаружения бота
TOKEN = os.environ.get("BOT_TOKEN")

#Сам пост для определения id пользователя
POST_ID = 703181529106481153

#Правила для ролей
ROLES = {
    '🎮': 698114408706080809, # Геймер
    '🥋': 698114726902628374, # Ученик
    '📖': 703176163865919578, # Учитель
    '💎': 703175870055055413, # Совет лицея

}

#Добавление админов, т.е. беск. кол-во ролей
EXCROLES = ()

#Максимум ролей
MAX_ROLES_PER_USER = 4
