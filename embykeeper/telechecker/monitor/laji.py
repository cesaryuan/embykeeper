from pyrogram.types import Message

from .base import Monitor


class LajiMonitor(Monitor):
    name = "laji"
    chat_keyword = r"[a-zA-Z0-9]{21}"
    # chat_keyword = r"hWVsG1Yadnchd82c7JX5O"
    # chat_keyword = r"RJU1PGzlBXvQCjX1dFBys"
    bot_username = "zckllflbot"
    # chat_name = "-965261929"
    chat_name = "-1001549608772"
    notify_create_name = True
    allow_edit = False

    async def on_trigger(self, message: Message, key, reply):
        await self.client.send_message(self.bot_username, f"/key {key}")
        await self.client.send_message(self.bot_username, self.unique_name)
        self.log.bind(notify=True).info(f'已向垃圾影音Bot @{self.bot_username} 发送邀请码: "{key}", 请查看.')
