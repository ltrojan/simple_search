import uuid
import collections

from simple_search import language


class DataItem(object):

    def __init__(self, name, text, tok=None):
        if tok is None:
            tok = language.simple_tokenizer
        self.name = name
        self.text = text
        self.tokens = tok(text)

    def __iter__(self):
        return iter([self.name, self.text])

    def __contains__(self, keys):
        return all(key in self.tokens for key in keys)

    def __repr__(self):
        return "DataItem: -{}-".format(self.name)

    def __str__(self):
        return self.__repr__()


class DataBaseDict(dict):

    def uids(self):
        return self.keys()

    def __setitem__(self, uid, item):
        uid = str(uid)
        if uid in self:
            print("WARNING: uid already in db")
        dict.__setitem__(self, uid, DataItem(*item))

    def update(self, data):
        data = dict(data)
        if any(uid in self for uid in data.uids()):
            print("WARNING: uid already in db")
        dict.update(self, data)

    @classmethod
    def from_rows(cls, rows):
        db = cls()
        db.append_rows(rows)
        return db

    def append_row(self, row):
        uid = row[0]
        self[uid] = row[1:]

    def append_rows(self, rows):
        for row in rows:
            self.append_row(row)

    def to_rows(self):
        return ((uid, ) + item for uid, item in self.items())

    def filter(self, fun=None):
        return DataBaseDict((uid, item) for uid, item in self.items() if fun(item))

    def filter_keys(self, keys):
        fun = lambda item: keys in item
        return self.filter(fun)
