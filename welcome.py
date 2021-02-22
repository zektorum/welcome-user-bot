from random import randint
from vk import vk_bot


def send_message_to_chat(chat_id: int, message: str, attachment=None):
    """ Отправка сообщения в беседу от имени сообщества """
    values = {
        "chat_id": chat_id,
        "message": message,
        "random_id": randint(0, 100000000),
        "attachment": attachment
    }
    vk_bot.method("messages.send", values)


def is_added(raw):
    """ Ищет в сообщении информацию о том, был ли приглашён пользователь """
    try:
        if raw["object"]["message"]["action"]["type"] in ["chat_invite_user", "chat_invite_user_by_link"]:
            return raw["object"]["message"]["action"]["member_id"]
    except KeyError:
        return False
