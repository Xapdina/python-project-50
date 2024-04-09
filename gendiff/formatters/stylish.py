from gendiff.const import INDENT, DIFF_CHANGES_TYPES


def build_indent(depth):
    return INDENT[:-2] + INDENT * depth


def format_data_to_stylish(data, depth):
    string_data = '\n'.join(data)
    last_indent = build_indent(depth)[:-2]
    return f'{string_data}\n{last_indent}'


def put_into_braces(formatted_data):
    return f'{{\n{formatted_data}}}'


def to_string(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'{build_indent(depth)}  '
                         f'{key}: {to_string(val, depth + 1)}')
        lines_string = format_data_to_stylish(lines, depth)
        return put_into_braces(lines_string)
    return value


def render_stylish(data):
    def _iter_stylish(data, depth=0):
        result = []
        for key, value in data.items():
            match value['type']:
                case DIFF_CHANGES_TYPES.DELETED:
                    result.append(f'{build_indent(depth)}- {key}: '
                                  f'{to_string(value["value"], depth + 1)}')
                case DIFF_CHANGES_TYPES.ADDED:
                    result.append(f'{build_indent(depth)}+ {key}: '
                                  f'{to_string(value["value"], depth + 1)}')
                case DIFF_CHANGES_TYPES.MODIFIED:
                    result.append(f'{build_indent(depth)}- {key}: '
                                  f'{to_string(value["old_value"], depth + 1)}')  # noqa
                    result.append(f'{build_indent(depth)}+ {key}: '
                                  f'{to_string(value["new_value"], depth + 1)}')  # noqa
                case DIFF_CHANGES_TYPES.UNCHANGED:
                    result.append(f'{build_indent(depth)}  {key}: '
                                  f'{to_string(value["old_value"], depth + 1)}')  # noqa
                case DIFF_CHANGES_TYPES.NESTED:
                    result.append(f'{build_indent(depth)}  {key}: '
                                  f'{_iter_stylish(value["children"], depth + 1)}')  # noqa
                case _:
                    raise ValueError(f'Unknown type: {value["type"]}')

        result_string = format_data_to_stylish(result, depth)
        return put_into_braces(result_string)

    return _iter_stylish(data)
