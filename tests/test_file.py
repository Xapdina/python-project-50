#!/usr/bin/env python3
import os
from gendiff.gendiff import generate_diff


def get_fixtures_path(file_name):
    return os.path.join('tests/fixtures', file_name)


def get_fixtures_data(file_name):
    with open(get_fixtures_path(file_name), 'r') as f:
        return f.read()


def test_generate_diff_json():
    res = generate_diff(
        get_fixtures_path('file1.json'),
        get_fixtures_path('file2.json')
    )

    expected = get_fixtures_data(
        'file_json_answer.txt')

    assert res == expected