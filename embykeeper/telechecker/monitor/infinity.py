from pyrogram.types import Message

from .base import Monitor


class InfinityMonitor(Monitor):
    name = "infinity"
    chat_keyword = r"register-[-\w]{36}"
    # chat_keyword = r"hWVsG1Yadnchd82c7JX5O"
    # chat_keyword = r"RJU1PGzlBXvQCjX1dFBys"
    bot_username = "Infinity94bot"
    # chat_name = "-965261929"
    chat_name = "-1001590509501"
    notify_create_name = True
    allow_edit = False

    async def on_trigger(self, message: Message, key, reply):
        await self.client.send_message(self.bot_username, f"/invite {key}")
        await self.client.send_message(self.bot_username, f"/create {self.unique_name}")
        self.log.bind(notify=True).info(f'已向 infinity Bot @{self.bot_username} 发送邀请码: "{key}", 请查看.')
