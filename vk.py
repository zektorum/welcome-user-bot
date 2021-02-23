from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from const import GROUP_ID, BOT_TOKEN


vk_bot = VkApi(token=BOT_TOKEN)
vk_bot._auth_token()
vk_bot.get_api()
bot_longpoll = VkBotLongPoll(vk_bot, GROUP_ID)


NEW_MESSAGE_EVENT = VkBotEventType.MESSAGE_NEW
