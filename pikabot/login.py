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
from telethon import events 
from pikabot.Event_Handlers.login_client import pika_login 

async def pika_msg(_pika, text, _pika_=None, parse_mode=None, link_preview=None):
  parse_mode = parse_mode or "md"; link_preview = link_preview or False
  if _pika_ is None:
      return await _pika.edit(text, parse_mode=parse_mode, link_preview=link_preview)
  else:
      return await _pika.reply(text, parse_mode=parse_mode,link_preview=link_preview)
