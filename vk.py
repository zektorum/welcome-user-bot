# welcome_user_bot
# Copyright © 2021 Murad Murtuzaliev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from args import GROUP_ID, TOKEN
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_bot = VkApi(token=TOKEN)
vk_bot._auth_token()
vk_bot.get_api()
bot_longpoll = VkBotLongPoll(vk_bot, GROUP_ID)


NEW_MESSAGE_EVENT = VkBotEventType.MESSAGE_NEW
