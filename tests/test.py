import os
from gendiff.gendiff import generate_diff


def get_fixtures_data(file_name):
    path_to_file = os.path.join('fixtures', file_name)
    with open(path_to_file, 'r') as f:
        return f.read()


def test_generate_diff():
    res = generate_diff(
        get_fixtures_data('file1.json'),
        get_fixtures_data('file2.json'))

    expected = get_fixtures_data(
        'file_ans')

    assert res == expected
