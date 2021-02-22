from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.longpoll import VkLongPoll

from const import GROUP_ID, GROUP_TOKEN, BOT_TOKEN, SERVICE_TOKEN


# Авторизация токена бота для работы с пользователем-администратором
vk_bot = VkApi(token=BOT_TOKEN)
vk_bot._auth_token()
vk_bot.get_api()
bot_longpoll = VkBotLongPoll(vk_bot, GROUP_ID)


# Авторизация токена группы для рассылки сообщений пользователям
vk_group = VkApi(token=GROUP_TOKEN)
vk_group._auth_token()
vk_group.get_api()
group_longpoll = VkLongPoll(vk_group)


# Авторизация токена приложения для получения количества репостов
vk_service = VkApi(token=SERVICE_TOKEN)
vk_service._auth_token()
vk_service.get_api()