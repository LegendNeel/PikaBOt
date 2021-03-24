"""
{i}get_id <reply to msg/media> 
**Usage**: Get ID of any Telegram media, Group, or any user\n
{i}info @username/reply to user msg
**Usage**: Get full User information
"""

from Asst_modules import ItzSjDude, pikatgbot, _getinfo, _getid

@ItzSjDude(pika=True, pattern="info(.*)")
@pikatgbot('AmIAdm')
@pikatgbot('AdmOnly')
async def _(event):
    await _getinfo(event)

@ItzSjDude(pika=True, pattern="get_id(.*)")
@pikatgbot('AmIAdm')
@pikatgbot('AdmOnly')
async def _(event):
    await _getid(event)
