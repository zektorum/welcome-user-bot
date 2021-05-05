from time import sleep
from datetime import datetime

from vk import bot_longpoll as longpoll
from vk import NEW_MESSAGE_EVENT
from tools import *


def event_loop():
    """ Цикл обработки событий. Прилашённым пользователям отправляется приветствие """
    for event in longpoll.check():
        try:
            if event.from_chat:
                if event.type == NEW_MESSAGE_EVENT:
                    user_id = get_user_id(event.raw)
                    if user_id:
                        first_name = get_user_name_by_id(user_id)[0]
                        send_message(event.chat_id, f"Welcome, [id{user_id}|{first_name}]!")
        except AttributeError:
            print("Ошибка! Получено событие из сообщений сообщества. Ожидалось из беседы")
            sleep(5)
            continue


def main():
    sending_time = generate_sending_time()
    user_id = get_random_user()
    is_generated = True
    while True:
        if longpoll.check():  # Если есть события
            event_loop()
        elif is_generated and sending_time == datetime.now().strftime("%H:%M"):
            send_hello_to_user(user_id)
            is_generated = False
        elif not is_generated:
            user_id = get_random_user()
            sending_time = generate_sending_time()
            is_generated = True


if __name__ == "__main__":
    main()
