"""Android Related Commands
{i}magisk
**Usage**:Get latest Magisk releases\n
{i}device <codename>
**Usage**: Get info about android device codename or model.\n
{i}codename <brand> <device>
**Usage**: Search for android device codename.\n
{i}specs <brand> <device>
**Usage**: Get device specifications info.\n
{i}twrp <codename>
**Usage**: Get latest twrp download for android device.\n"""

from Asst_modules import ItzSjDude, pikatgbot, magisk, device_info, codename_info, dspecs, twrp

@ItzSjDude(pika=True, pattern="magisk$")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(request):
    await magisk(request)


@ItzSjDude(pika=True, pattern=r"device(?: |$)(\S*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(request):
    await device_info(request)


@ItzSjDude(pika=True, pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(request):
    await codename_info(request)


@ItzSjDude(pika=True, pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(request):
    await dspecs(request)


@ItzSjDude(pika=True, pattern=r"twrp(?: |$)(\S*)")
@pikatgbot("AmIAdm")
@pikatgbot("AdmOnly")
async def _(request):
    await twrp(request)
