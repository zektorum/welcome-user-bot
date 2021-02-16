from random import randint
from time import sleep

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll
import vk_api

from const import GROUP_ID, GROUP_TOKEN, BOT_TOKEN, SERVICE_TOKEN

# Авторизация токена бота для работы с пользователем-администратором
vk_bot = vk_api.VkApi(token=BOT_TOKEN)
vk_bot._auth_token()
vk_bot.get_api()
longpoll = VkBotLongPoll(vk_bot, GROUP_ID)

# Авторизация токена приложения для получения количества репостов
vk_service = vk_api.VkApi(token=SERVICE_TOKEN)
vk_service._auth_token()
vk_service.get_api()

# Авторизация токена группы для рассылки сообщений пользователям
# vk_group = vk_api.VkApi(token=GROUP_TOKEN)
# vk_group._auth_token()
# vk_group.get_api()
# longpoll = VkLongPoll(vk_group)


# FIXME: не возвращает ничего
def get_list_of_repost_users(post_id: int):
    """ Получение списка пользователей, репостнувших запись """
    values = {
        "owner_id": -195382217,
        "post_id": post_id,
        "count": 1000
    }
    return vk_service.method("wall.getReposts", values)


def send_message_to_chat(chat_id: int, message: str, attachment=None):
    """ Отправка сообщения в беседу от имени сообщества """
    values = {
        "chat_id": chat_id,
        "message": message,
        "random_id": randint(0, 100000000),
        "attachment": attachment
    }
    vk_bot.method("messages.send", values)


# TODO: протестировать работоспособность функции
def send_message_to_user(user_id: int, message: str, attachment=None):
    """ Отправка сообщения пользователю от имени сообщества """
    values = {
        "user_id": user_id,
        "message": message,
        "random_id": randint(0, 100000000),
        "attachment": attachment
    }
    vk_bot.method("messages.send", values)


def main():
    while True:
        print("bot is online")
        try:
            for event in longpoll.listen():
                if event.from_chat:
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        print(event.message.text)
                        print(get_list_of_repost_users(283))
        except AttributeError:
            print("Ошибка! Получено событие из сообщений сообщества. Ожидалось из беседы")
            sleep(5)
            continue


if __name__ == "__main__":
    main()
