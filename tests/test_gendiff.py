import os
from gendiff import generate_diff

TEST_DATA = os.path.join(os.path.dirname(__file__), 'test_data')


def get_path(filename):
    return os.path.join(TEST_DATA, filename)


def test_flat_json():
    expected = open(get_path('result_flat_json.txt')).read()
    result = generate_diff(get_path('file1.json'), get_path('file2.json'))
    assert result == expected