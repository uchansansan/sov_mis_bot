import requests

offset = 0 # параметр необходим для подтверждения обновления
URL = 'https://api.telegram.org/bot' # URL на который отправляется запрос
TOKEN = '452339224:AAF1ob9OVl9P5ZGD0gUvKevUEdfZzLt3r3s' # токен  бота, полученный от @BotFather
data = {'offset': offset  1, 'limit': 0, 'timeout': 0}

try: # обрабатываем исключения
    request = requests.post(URL  TOKEN  '/getUpdates', data=data) # собственно сам запрос
except:
    print('Error getting updates')
    return False

if not request.status_code == 200: return False # проверяем пришедший статус ответа
if not request.json()['ok']: return False


for update in request.json()['result']:
    offset = update['update_id'] #  подтверждаем текущее обновление

    if 'message' not in update or 'text' not in update['message']: # это просто текст или какая-нибудь картиночка?
        print('Unknown message')
        continue

    message_data = { # формируем информацию для отправки сообщения
        'chat_id': update['message']['chat']['id'], # куда отправляем сообщение
        'text': "I'm <b>bot</b>", # само сообщение для отправки
        'reply_to_message_id': update['message']['message_id'], # если параметр указан, то бот отправит сообщение в reply
        'parse_mode': 'HTML' # про форматирование текста ниже
    }

    try:
        request = requests.post(URL  TOKEN  '/sendMessage', data=message_data) # запрос на отправку сообщения
    except:
        print('Send message error')
        return False

    if not request.status_code == 200: # проверим статус пришедшего ответа
        return False


while True:
    try:
        check_updates()
    except KeyboardInterrupt: # порождается, если бота остановил пользователь
        print('Interrupted by the user')
        break