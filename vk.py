import sys

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_bot = VkApi(token=str(sys.argv[3]))
vk_bot._auth_token()
vk_bot.get_api()
bot_longpoll = VkBotLongPoll(vk_bot, int(sys.argv[2]))


NEW_MESSAGE_EVENT = VkBotEventType.MESSAGE_NEW
