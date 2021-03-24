# © 2020 PikaBot
#
# You may not use this file without proper authorship and consent from @ItzSjDudeSupport
#
# Made by @ItzSjDude for Pikabot

try:
    from pikabot.sql_helper import SESSION, BASE
except ImportError:
    raise Exception("Hello!")

from sqlalchemy import *

class GMute(BASE):
    __tablename__ = "gmute"
    sender = Column(String(14), primary_key=True)
    pika_id = Column(Numeric, primary_key=True)
    def __init__(self, sender, pika_id):
        self.sender = str(sender)
        self.pika_id = pika_id 

GMute.__table__.create(checkfirst=True)

class GBan(BASE):
    __tablename__ = "gban"
    sender = Column(String(14), primary_key=True)
    pika_id = Column(Numeric, primary_key=True)
    reason = Column(UnicodeText)
    def __init__(self, sender, pika_id, reason=""):
        self.sender = str(sender)
        self.pika_id = str(pika_id) 
        self.reason = reason 

GBan.__table__.create(checkfirst=True)
       
def is_gbanned(sender, pika_id):
    try: 
        _pikaG = SESSION.query(GBan).get((str(sender), str(pika_id)))
        if _pikaG:
            return str(_pikaG.reason)
    finally:
        SESSION.close()


def gban(sender, pika_id, reason):
    adder = GBan(str(sender), str(pika_id), str(reason))
    SESSION.add(adder)
    SESSION.commit()


def ungban(sender, pika_id):
    rem = SESSION.query(GBan).get((str(sender), str(pika_id)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit() 

def is_gmuted(sender):
    try:
        return SESSION.query(GMute).all()
    except: 
        return None
    finally:
        SESSION.close()


def gmute(sender, pika_id):
    adder = GMute(str(sender), pika_id)
    SESSION.add(adder)
    SESSION.commit()


def ungmute(sender, pika_id):
    rem = SESSION.query(GMute).get((str(sender), pika_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

