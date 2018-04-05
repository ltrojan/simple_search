_def_sep = ','


def items_num(items, sep=None, num=None):
    if num is None:
        return items
    if sep is None:
        sep = _def_sep
    return items[:num-1] + [sep.join(items[num:])]


def split_items(line, sep=None, num=None):
    """ Split a csv line in a number of items
    """
    if sep is None:
        sep = _def_sep
    line = line.split(sep)
    return items_num(line, sep=sep, num=num)


def parse_item(item):
    return item.strip("\"")


def parse_line(line, num=None):
    return list(map(parse_item, split_items(line.strip(), num=num)))


def parse_stream(stream, num=None):
    return (parse_line(line, num=num) for line in stream)


def parse_file(path):
    with open(path, 'r') as fid:
       for line in fid:
           yield parse_line(line, num=3)
