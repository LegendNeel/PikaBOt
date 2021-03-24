"""**pastebin like site**\n
{i}paste <reply to file/msg>"""

from Asst_modules import _deldog

@ItzSjDude(pika=True, pattern="paste ?(.*)")
@pikatgbot('AdmOnly')
async def _(event):
    await _deldog(event)
