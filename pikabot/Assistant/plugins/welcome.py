"""
{i}setwelcome <welcome message> or reply to msg
**Usage**: Sets the message as a welcome note in the chat
{i}getwelcome 
**Usage**: Shows current welcome note in the chat\n
{i}delwelcome 
**Usage**: Deletes the welcome note from current chat\n\n 
**Available formats for formatting welcome Note**:
`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`
"""

from Asst_modules import ItzSjDude, pikatgbot, ChatAction, _welcome, del_welcm, get_welcm, set_wlcm, clean_welcm, tgbot, pikatgbot


@tgbot.on(ChatAction)
async def _(_pika):
    await _welcome(_pika)


@ItzSjDude(pika=True, pattern=r"setwelcome(?: |$)(.*)")
@pikatgbot("OwnSudo")
async def _(_pika):
    await set_wlcm(_pika)


@ItzSjDude(pika=True, pattern="getwelcome$")
@pikatgbot("OwnSudo")
async def _(_pika):
    await get_welcm(_pika)


@ItzSjDude(pika=True, pattern="delwelcome$")
@pikatgbot("OwnSudo")
async def _(_pika):
    await del_welcm(_pika)

@ItzSjDude(pika=True, pattern="cleanwelcome$")
@pikatgbot("OwnSudo")
async def _(_pika):
    await clean_welcm(_pika)
