#    Copyright (C) 2024  BDB0B Source
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    T.me/BDB0B - T.me/zzzzl1l
try:
    from . import BASE, SESSION
except ImportError as e:
    raise Exception("Memes For BDB0B") from e
from sqlalchemy import Column, Numeric, String, UnicodeText


class BDB0BMemes(BASE):
    __tablename__ = "BDB0B_funs"
    meme_txt = Column(String(255), primary_key=True)
    meme_id = Column(String(255))

    def __init__(self, meme_txt, meme_id):
        self.meme_txt = str(meme_txt)
        self.meme_id = str(meme_id)

BDB0BMemes.__table__.create(bind=SESSION.get_bind(), checkfirst=True)


def get_alll_memes():
    try:
        return SESSION.query(BDB0BMemes).all()
    finally:
        SESSION.close()


def get_memes(meme_txt):
    memes = SESSION.query(BDB0BMemes).get(str(meme_txt))
    if memes:
        return memes.meme_id
    else:
        return None


def add_memes(meme_txt, meme_id):
    memes = BDB0BMemes(str(meme_txt), str(meme_id))
    SESSION.add(memes)
    SESSION.commit()


def remove_memes(meme_txt):
    memes = SESSION.query(BDB0BMemes).get(str(meme_txt))
    if memes:
        SESSION.delete(memes)
        SESSION.commit()


def remove_all_memes():
    saved_memes = SESSION.query(BDB0BMemes)
    if saved_memes:
        saved_memes.delete()
        SESSION.commit()
