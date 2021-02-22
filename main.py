from time import sleep
from vk_api.bot_longpoll import VkBotEventType
from vk import bot_longpoll as longpoll


def main():
    while True:
        print("bot is online")
        try:
            for event in longpoll.listen():
                if event.from_chat:
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        print(event.message.text)
        except AttributeError:
            print("Ошибка! Получено событие из сообщений сообщества. Ожидалось из беседы")
            sleep(5)
            continue
        except Exception as e:
            print(e.args[0])
            break


if __name__ == "__main__":
    main()
