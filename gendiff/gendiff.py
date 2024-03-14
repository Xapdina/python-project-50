#!/usr/bin/env python3
import json
import yaml


def to_str(value):
    return str(value).lower()


def generate_diff(file_path1, file_path2):
    data1 = file_path1
    data2 = file_path2

    if file_path1.endswith('.json'):
        data1 = json.load(open(file_path1))
        data2 = json.load(open(file_path2))
    elif file_path1.endswith('.yaml'):
        data1 = yaml.safe_load(open(file_path1))
        data2 = yaml.safe_load(open(file_path2))
    else:
        print('Unsupported file type')

    diff = []
    keys = sorted((data1.keys() | data2.keys()))

    for key in keys:
        value_data1 = data1.get(key)
        value_data2 = data2.get(key)

        if key not in data2:
            diff.append(f' - {key}: {to_str(value_data1)}')
        elif key not in data1:
            diff.append(f' + {key}: {to_str(value_data2)}')
        elif key in data1 and data2 and value_data1 != value_data2:
            diff.append(f' - {key}: {to_str(value_data1)}')
            diff.append(f' + {key}: {to_str(value_data2)}')
        else:
            diff.append(f'   {key}: {to_str(value_data2)}')

    return '{\n' + '\n'.join(diff) + '\n}'


if __name__ == '__main__':
    print(generate_diff('/Users/daniilbagaturia/python-project-50/tests/fixtures/file1.yaml',
                        '/Users/daniilbagaturia/python-project-50/tests/fixtures/file2.yaml'))
