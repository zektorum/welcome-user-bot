from random import randint
from vk import vk_bot, vk_service


# FIXME: не возвращает ничего
def get_list_of_repost_users(post_id: int):
    """ Получение списка пользователей, репостнувших запись """
    values = {
        "owner_id": -195382217,
        "post_id": post_id,
        "count": 1000
    }
    return vk_service.method("wall.getReposts", values)


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
