"""
{i}app <appname>
{i}tm <as reply to a media>
{i}tt <as reply to a large text>
"""
from Asst_modules import ItzSjDude, pikatgbot, _invite, _telegraph, apk

@ItzSjDude(pika=True, pattern="app (.*)")
@pikatgbot('AdmOnly')
@pikatgbot('AmIAdm')
async def _(e):
    await apk(e)

@ItzSjDude(pika=True, pattern="t(m|t) ?(.*)")
@pikatgbot('AmIAdm')
async def _(event):
    await _telegraph(event)
