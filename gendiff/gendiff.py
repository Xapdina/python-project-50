from gendiff.diff_parser import diff_parser
from formatter import formatter_for_diff
from gendiff.parser import file_parser
import os


def get_file_format(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]


def get_file(file_path):
    with open(file_path) as file:
        return file_parser(file, get_file_format(file_path))


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = get_file(file_path1)
    data2 = get_file(file_path2)
    diff = diff_parser(data1, data2)
    return formatter_for_diff(diff, formatter)
