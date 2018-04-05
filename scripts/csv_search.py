#!/usr/bin/env python3

import argparse

from simple_search import parse_csv
from simple_search import database


def dict_prep(data):
    return ["{}: {}".format(uid, item.name) for uid, item in data.items()]


def dict_join(data):
    return "\n".join(dict_prep(data))


def get_rows(path, keywords=None):
    if keywords is None:
        return {}
    if len(keywords) == 0:
        return {}
    rows = parse_csv.parse_file(path)
    db = database.DataBaseDict.from_rows(rows)
    ret = db.filter_keys(keywords)
    return ret


def main(path, keywords=None):
    print(dict_join(get_rows(path, keywords=keywords)))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Simple Search')
    parser.add_argument('path', help='path to an existing CSV file')
    parser.add_argument('keywords', nargs='+')
    args = parser.parse_args()

    main(args.path, keywords=args.keywords)
