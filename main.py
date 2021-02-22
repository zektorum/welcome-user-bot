from time import sleep
from vk import bot_longpoll as longpoll
from vk import NEW_MESSAGE_EVENT

from welcome import is_added, send_message_to_chat


def main():
    while True:
        print("bot is online")
        try:
            for event in longpoll.listen():
                if event.from_chat:
                    if event.type == NEW_MESSAGE_EVENT:
                        if is_added(event.raw):
                            send_message_to_chat(event.chat_id, "Welcome, Murad!")
        except AttributeError:
            print("Ошибка! Получено событие из сообщений сообщества. Ожидалось из беседы")
            sleep(5)
            continue
        except Exception as e:
            print(e.args[0])
            break


if __name__ == "__main__":
    main()
