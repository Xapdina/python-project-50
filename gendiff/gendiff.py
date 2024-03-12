#!/usr/bin/env python3
import argparse
import json


def parser_args(file_path1=None, file_path2=None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True,
        prog='gendiff'
    )
    parser.add_argument(file_path1)
    parser.add_argument(file_path2)
    parser.add_argument('-f', '--format', help='set format of output')
    arg = parser.parse_args()
    print(arg)


def to_str(value):
    return str(value).lower()


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    diff = []

    for key in sorted(data1.keys() | data2.keys()):
        if key not in data2:
            diff.append(f'- {key}: {to_str(data1[key])}')
        elif key not in data1:
            diff.append(f'+ {key}: {to_str(data2[key])}')
        elif key in data1 and data2 and data1[key] != data2[key]:
            diff.append(f'- {key}: {to_str(data1[key])}')
            diff.append(f'+ {key}: {to_str(data2[key])}')
        else:
            diff.append(f'  {key}: {to_str(data2[key])}')

    stail_diff = "\n ".join(diff)

    return f'{{\n {stail_diff}\n}}'


if __name__ == '__main__':
    print(generate_diff('/Users/daniilbagaturia/python-project-50/file_dir/file1.json',
                        '/Users/daniilbagaturia/python-project-50/file_dir/file2.json'))
