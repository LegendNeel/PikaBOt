"""
{i}pika
**Usage**: Checks Ping Speed
"""

# Made by @ItzSjDude for Pikabot
from Asst_modules import ItzSjDude, pikatgbot, _ping


@ItzSjDude(pika=True, pattern="pika$")
async def _(event):
    await _ping(event)
