"""
{i}set|get|del var <VarName>
**Usage**: set|get|del Heroku Vars\n
{i}usage
**Usage**: Shows Dynos usage\n
{i}logs
**Usage**: Sends your botlogs in current chat\n
{i}restart
**Usage**: Restarts Pikabot
"""

from Asst_modules import ItzSjDude, pikatgbot, _dyno, _logs, _restart, _vars

@ItzSjDude(pika=True, pattern=r"(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)")
@pikatgbot('OwnSudo')
async def _(var):
    await _vars(var)


@ItzSjDude(pika=True, pattern=r"usage(?: |$)")
@pikatgbot('OwnSudo')
async def _(dyno):
    await _dyno(dyno)


@ItzSjDude(pika=True, pattern="restart")
@pikatgbot('OwnSudo')
async def _(rstrt):
    await _restart(rstrt)


@ItzSjDude(pika=True, pattern=r"logs")
@pikatgbot('OwnSudo')
async def _(dyno):
    await _logs(dyno)
