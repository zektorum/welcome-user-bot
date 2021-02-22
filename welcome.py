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