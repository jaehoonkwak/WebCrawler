from unittest.mock import patch, mock_open
from main.file_reader import get_urls


def test_get_urls_SHOULD_return_None_WHEN_file_does_NOT_exist():
    assert get_urls("Invalid_file_name") is None


def test_get_urls_SHOULD_return_None_WHEN_exception_occurred_in_file_open():
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = IOError
        assert get_urls("test_input.txt") is None


def test_get_urls_SHOULD_return_URLs_WHEN_normal_cases():
    urls = get_urls("test_input.txt")
    assert urls is not None
    assert len(urls) == 1
    assert urls[0] == 'www.naver.com'
