import os
import pytest
from gendiff.gendiff import generate_diff


def get_fixtures_path(file_name):
    return os.path.join('tests/fixtures', file_name)


def get_fixtures_data(file_name):
    with open(get_fixtures_path(file_name), 'r') as f:
        return f.read()


@pytest.mark.parametrize('file1, file2, answer', [
    ('file1.json', 'file2.json', 'file_json_answer.txt'),
    ('file1.yaml', 'file2.yaml', 'file_yml_answer.txt'),
])
def test_generate_diff(file1, file2, answer):
    res = generate_diff(
        get_fixtures_path(file1),
        get_fixtures_path(file2)
    )

    expected = get_fixtures_data(
        answer)

    assert res == expected
