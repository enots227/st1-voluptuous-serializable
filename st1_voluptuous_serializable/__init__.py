from typing import List
from voluptuous import MultipleInvalid, DictInvalid


def voluptuous_dict_loop(path: List[str], error_message: str):
    res = {}

    if len(path) == 0:
        return error_message

    segment = str(path[0])

    if len(path) > 1:
        res[segment] = voluptuous_dict_loop(path[1:], error_message)
    else:
        res[segment] = error_message

    return res

def voluptuous_dict(invalids: MultipleInvalid):
    negs = {}

    for invalid in invalids.errors:
        if isinstance(invalid, DictInvalid):
            return { 'root': invalid.msg }

        segment = str(invalid.path[0])

        negs[segment] = voluptuous_dict_loop(invalid.path[1:], invalid.error_message)
    
    return negs

