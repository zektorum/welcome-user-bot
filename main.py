from datetime import datetime
from time import sleep
import sys

from tools import *
from vk import NEW_MESSAGE_EVENT
from vk import bot_longpoll as longpoll


def event_loop(events: list):
    """ Цикл обработки событий. Прилашённым пользователям отправляется приветствие """
    for event in events:
        try:
            if event.from_chat:
                if event.type == NEW_MESSAGE_EVENT:
                    user_id = get_user_id(event.raw)
                    if user_id:
                        first_name = get_user_name_by_id(user_id)[0]
                        message = f"Welcome, [id{user_id}|{first_name}]!"
                        send_message(event.chat_id, message)
                        print(f"Пользователю {user_id} отправлено сообщение: {message}")
        except AttributeError:
            print("Ошибка! Получено событие из сообщений сообщества. Ожидалось из беседы")
            sleep(5)
            continue


def main():
    sending_time = generate_sending_time()
    user_id = get_random_user()
    events = longpoll.check()
    is_generated = True
    while True:
        if events:  # Если есть события
            event_loop(events)
            events = longpoll.check()
        elif is_generated and sending_time == datetime.now().strftime("%H:%M"):
            send_hello_to_user(user_id)
            is_generated = False
        elif not is_generated:
            user_id = get_random_user()
            sending_time = generate_sending_time()
            is_generated = True


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print(f"Ошибка! Ожидалось 3 аргумента, получено {argc - 1}")
        sys.exit(1)

    main()
