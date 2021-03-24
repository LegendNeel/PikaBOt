#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 
"""
{i}bash <cmd> 
*"Usage**: For executing linux/Gnu Commands\n 
{i}eval <code> 
*"Usage**: For executing short python codes\n"""
from Asst_modules import ItzSjDude, pikatgbot, _eval, _bash 


@ItzSjDude(pika=True, pattern="bash ?(.*)")
@pikatgbot('OwnSudo')
async def _(event):
    await _bash(event)

@ItzSjDude(pika=True, pattern="eval ?(.*)")
@pikatgbot('OwnSudo')
async def _(event):
  await _eval(event)
