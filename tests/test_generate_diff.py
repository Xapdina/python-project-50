import os
import pytest
from gendiff.gen_diff import generate_diff
from gendiff.const import STYLE_FORMATS


def get_fixtures_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', file_name)


def get_fixtures_data(file_name):
    with open(get_fixtures_path(file_name), 'r') as f:
        return f.read()


@pytest.mark.parametrize('file1, file2', [
    ('file1.json', 'file2.json'),
    ('file1.json', 'file2.yaml'),
    ('file1.yaml', 'file2.json'),
    ('file1.yaml', 'file2.yaml')
])
def test_generate_diff(file1, file2):
    file_path1 = get_fixtures_path(file1)
    file_path2 = get_fixtures_path(file2)

    assert (generate_diff(file_path1, file_path2, STYLE_FORMATS.STYLISH)
            == get_fixtures_data('result_to_stylish'))
    assert (generate_diff(file_path1, file_path2)
            == get_fixtures_data('result_to_stylish'))
    assert (generate_diff(file_path1, file_path2, STYLE_FORMATS.PLAIN)
            == get_fixtures_data('result_to_plain'))
    assert (generate_diff(file_path1, file_path2, STYLE_FORMATS.JSON)
            == get_fixtures_data('result_to_json'))
    assert (generate_diff(file_path1, file_path2, STYLE_FORMATS.JSON)
            == get_fixtures_data('result_to_yaml'))


@pytest.mark.parametrize('file1, file2', [
    ('file1.json', 'file2.json'),
    ('file1.json', 'file2.yaml'),
    ('file1.yaml', 'file2.json'),
    ('file1.yaml', 'file2.yaml')
])
def test_invalid_format(file1, file2):
    file_path1 = get_fixtures_path(file1)
    file_path2 = get_fixtures_path(file2)

    with pytest.raises(ValueError):
        generate_diff(file_path1, file_path2, 'invalid_format')
