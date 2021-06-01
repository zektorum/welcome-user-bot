from args import GROUP_ID, TOKEN
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_bot = VkApi(token=TOKEN)
vk_bot._auth_token()
vk_bot.get_api()
bot_longpoll = VkBotLongPoll(vk_bot, GROUP_ID)


NEW_MESSAGE_EVENT = VkBotEventType.MESSAGE_NEW
