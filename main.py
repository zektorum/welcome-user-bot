from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from const import GROUP_ID, TOKEN

vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, GROUP_ID)

if __name__ == "__main__":
    while True:
        print("bot is online")
        for event in longpoll.listen():
            pass
