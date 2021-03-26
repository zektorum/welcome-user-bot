from random import randint

from vk import vk_bot


def send_message(chat_id: int, message: str, attachment=None):
    """ Отправка сообщения в беседу от имени сообщества """
    values = {
        "chat_id": chat_id,
        "message": message,
        "random_id": randint(0, 100000000),
        "attachment": attachment
    }
    vk_bot.method("messages.send", values)


def get_user_id(raw: dict):
    """ Возвращает id пользователя, если он был приглашён """
    try:
        if raw["object"]["message"]["action"]["type"] in ["chat_invite_user", "chat_invite_user_by_link"]:
            return raw["object"]["message"]["action"]["member_id"]
    except KeyError:
        return None


def get_user_name_by_id(user_id: int):
    """ Получает инициалы пользователя по id"""
    result = vk_bot.method("users.get", {"user_ids": user_id})[0]
    return result["first_name"], result["last_name"]


def get_users_list(chat_id: int) -> list:
    """ Возвращает список из id пользователей беседы """
    response = vk_bot.method(
        "messages.getConversationMembers", {"peer_id": 2000000000 + chat_id}
    )
    return [i["member_id"] for i in response["items"]]
