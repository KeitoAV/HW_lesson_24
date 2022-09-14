import re
from typing import Iterator, List, Any


def get_query(cmd: str, val: str, file: Iterator) -> List[Any]:
    if cmd == 'filter':
        res = list(filter(lambda x: val in x, file))
        return res

    if cmd == 'map':
        res = list([x.split()[int(val)] for x in file])
        return res

    if cmd == 'unique':
        res = list(set(file))
        return res

    if cmd == 'sort':
        is_reverse = val == 'desc'
        res = sorted(file, reverse=is_reverse)
        return res

    if cmd == 'limit':
        res = list(file)[:int(val)]
        return res

    if cmd == "regex":
        # val = images\/(\w+|(\w+-\w+)|.{1,})\.png
        regex = re.compile(val)
        res = list(filter(lambda x: regex.search(x), file))
        return res

    return []

