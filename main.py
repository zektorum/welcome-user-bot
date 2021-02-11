from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll
import vk_api
from const import GROUP_ID, GROUP_TOKEN, BOT_TOKEN

# Авторизация токена бота для работы с пользователем-администратором
vk_bot = vk_api.VkApi(token=BOT_TOKEN)
vk_bot._auth_token()
vk_bot.get_api()
longpoll = VkBotLongPoll(vk_bot, GROUP_ID)

# Авторизация токена группы для рассылки сообщений пользователям
# vk_group = vk_api.VkApi(token=GROUP_TOKEN)
# vk_group._auth_token()
# vk_group.get_api()
# longpoll = VkLongPoll(vk_group)


def get_list_of_repost_users():
    """ Получение списка пользователей, репостнувших запись """
    pass


def send_message():
    """ Отправка сообщений """
    pass


def main():
    while True:
        print("bot is online")
        try:
            for event in longpoll.listen():
                if event.from_chat:
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        print(event.message.text)
        except AttributeError as e:
            print("Ошибка! Получено событие из сообщений сообщества. Ожидалось из беседы")
            continue


if __name__ == "__main__":
    main()
