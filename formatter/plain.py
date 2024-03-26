from gendiff.utils import DOT


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return value
    return f"'{str(value)}'"


def plain(diff_dict, path=''):
    lines = []

    for key, diff in diff_dict.items():
        value = diff.get('value')
        status = diff.get('status')
        if status == 'added':
            value = to_str(value)
            lines.append(f"Property '{path + key}' was added with value: '{value}'")
        elif status == 'deleted':
            lines.append(f"Property '{path + key}' was removed")
        elif status == 'updated':
            value1, value2 = map(to_str, value)
            item = path + key
            lines.append(f"Property '{item}' was updated. From {value1} to {value2}")
        elif isinstance(value, dict):
            lines.append(plain(value, path + key + DOT))
    return '\n'.join(lines)
