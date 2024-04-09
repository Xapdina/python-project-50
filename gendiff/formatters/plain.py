from gendiff.const import DIFF_CHANGES_TYPES


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return value
    return f"'{value}'"


def to_plain(diff):
    def _iter(diff, path=''):
        res = []
        for key, data in diff.items():
            current_path = f'{path}.{key}' if path else key
            match data['type']:
                case DIFF_CHANGES_TYPES.ADDED:
                    value = to_str(data['value'])
                    res.append(
                        f"Property '{current_path}' "
                        f"was added with value: {value}"
                    )
                case DIFF_CHANGES_TYPES.DELETED:
                    res.append(f"Property '{current_path}' was removed")

                case DIFF_CHANGES_TYPES.MODIFIED:
                    new_value = to_str(data['new_value'])
                    old_value = to_str(data['old_value'])
                    res.append(
                        f"Property '{current_path}' was updated. "
                        f"From {old_value} to {new_value}"
                    )
                case DIFF_CHANGES_TYPES.NESTED:
                    children = data['children']
                    res.extend(_iter(children, current_path))

                case DIFF_CHANGES_TYPES.UNCHANGED:
                    continue

                case _:
                    raise ValueError(f'Unsupported node type at {current_path}') # noqa

        return res

    return '\n'.join(_iter(diff))
