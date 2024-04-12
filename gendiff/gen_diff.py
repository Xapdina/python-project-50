from gendiff.build_diff import create_difference_tree
from gendiff.formatters import format_diff
from gendiff.parser import parse_data
from gendiff.const import DATA_FORMATS, STYLE_FORMATS
import os


def define_file_extension(file_path):
    extension = os.path.splitext(file_path)[1][1:]
    match extension:
        case 'json':
            return DATA_FORMATS.JSON
        case 'yml' | 'yaml':
            return DATA_FORMATS.YAML
        case _:
            raise ValueError(
                f'Unsupported extension: {extension}'
            )


def get_file_data(file_path):
    data_format = define_file_extension(file_path)
    with open(file_path) as file:
        data = file.read()
        return parse_data(data, data_format)


def generate_diff(file_path1, file_path2, formatter=STYLE_FORMATS.STYLISH):
    data1 = get_file_data(file_path1)
    data2 = get_file_data(file_path2)
    diff = create_difference_tree(data1, data2)
    return format_diff(diff, formatter)
