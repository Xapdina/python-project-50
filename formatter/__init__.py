from formatter.json import to_json
from formatter.plain import plain
from formatter.stylish import stylish


def formatter_for_diff(diff, formatter):
    match formatter:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return to_json(diff)
        case _:
            raise ValueError(f"Unsupported formatter: {formatter}")