from time import sleep

from vk import bot_longpoll as longpoll
from vk import NEW_MESSAGE_EVENT
from welcome import is_added, get_user_name_by_id, send_message_to_chat


def main():
    while True:
        print("bot is online")
        try:
            for event in longpoll.listen():
                if event.from_chat:
                    if event.type == NEW_MESSAGE_EVENT:
                        user_id = is_added(event.raw)
                        if user_id is not None:
                            first_name = get_user_name_by_id(user_id)[0]
                            send_message_to_chat(event.chat_id, f"Welcome, [id{user_id}|{first_name}]!")
        except AttributeError:
            print("Ошибка! Получено событие из сообщений сообщества. Ожидалось из беседы")
            sleep(5)
            continue


if __name__ == "__main__":
    main()
