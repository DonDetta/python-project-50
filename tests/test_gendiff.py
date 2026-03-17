import os
from gendiff import generate_diff

TEST_DATA = os.path.join(os.path.dirname(__file__), 'test_data')


def get_path(filename):
    return os.path.join(TEST_DATA, filename)


def test_flat_json():
    expected = open(get_path('result_flat_json.txt')).read()
    result = generate_diff(get_path('file1.json'), get_path('file2.json'))
    assert result == expected


def test_flat_yaml():
    expected = open(get_path('result_flat_json.txt')).read()
    result = generate_diff(get_path('file1.yml'), get_path('file2.yml'))
    assert result == expected


def test_nested_json():
    expected = open(get_path('result_nested.txt')).read().strip()
    result = generate_diff(get_path('file1_nested.json'), get_path('file2_nested.json'))
    assert result == expected


def test_nested_yaml():
    expected = open(get_path('result_nested.txt')).read().strip()
    result = generate_diff(get_path('file1_nested.yml'), get_path('file2_nested.yml'))
    assert result == expected


def test_plain():
    expected = open(get_path('result_plain.txt')).read().strip()
    result = generate_diff(
        get_path('file1_nested.json'),
        get_path('file2_nested.json'),
        'plain',
    )
    assert result == expected


def test_json():
    expected = open(get_path('result_json.txt')).read().strip()
    result = generate_diff(
        get_path('file1_nested.json'),
        get_path('file2_nested.json'),
        'json',
    )
    assert result == expected