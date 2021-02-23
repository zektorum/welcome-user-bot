from random import randint
from requests import get

from vk import vk_bot
from const import ACCESS_TOKEN


def get_list_of_repost_users(post_id: int):
    """ Получение списка пользователей, репостнувших запись """
    values = {
        "owner_id": -195382217,
        "post_id": post_id,
        "count": 1000,
        "access_token": ACCESS_TOKEN,
        "v": "5.130"
    }
    response = get("https://api.vk.com/method/wall.getReposts", params=values).json()
    users = []
    for user in response["response"]["items"]:
        if user["from_id"] > 0:
            users.append(user["from_id"])
    return users


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
