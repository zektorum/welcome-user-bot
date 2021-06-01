from random import choice, randint

from args import CHAT_ID
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


def get_user_id(raw: dict) -> str:
    """ Возвращает id пользователя, если он был приглашён """
    try:
        if raw["object"]["message"]["action"]["type"] in ["chat_invite_user", "chat_invite_user_by_link"]:
            return raw["object"]["message"]["action"]["member_id"]
    except KeyError:
        return ""


def get_user_name_by_id(user_id: str) -> tuple[str, str]:
    """ Получает инициалы пользователя по id"""
    result = vk_bot.method("users.get", {"user_ids": user_id})[0]
    return (result["first_name"], result["last_name"])


def get_users_list(chat_id: int) -> list[str]:
    """ Возвращает список из id пользователей беседы """
    response = vk_bot.method(
        "messages.getConversationMembers", {"peer_id": 2000000000 + int(chat_id)}
    )
    return [user["member_id"] for user in response["items"]]


def generate_sending_time():
    """ Возвращает строку в формате 'чч:мм' """
    return "{0}:{1}".format(randint(12, 19), randint(10, 59))


def get_random_user():
    """ Возвращает id случайного пользователя беседы """
    return choice([user_id for user_id in get_users_list(CHAT_ID) if user_id > 0])


def send_hello_to_user(user_id: str) -> None:
    """ Отправляет пользователю сообщение с одним из нескольких возможных вопросов """
    messages = ['Как дела?', 'Что нового?', 'Как настроение?']
    user_name = get_user_name_by_id(user_id)[0]
    send_message(CHAT_ID, f"Привет, [{user_id}|{user_name}]!" + choice(messages))

