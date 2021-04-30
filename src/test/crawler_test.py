from unittest.mock import patch, MagicMock
from main.crawler import Crawler


# Man in working
# How to mock to throw exception(ValueError) in urllib.request.urlopen()
# @patch('urllib.request.urlopen')
# def test_crawl_SHOULD_return_empty_list_WHEN_input_is_invalid_url(mocked_urlopen):
#     mocked_urlopen.return_value.side_effect = ValueError
#     crawler = Crawler()
#     crawler.set(1)
#
#     actual = crawler.crawl(['INVALID URL'])
#
#     assert actual is not None
#     assert type(actual) is list
#     assert len(actual) == 0


@patch('urllib.request.urlopen')
def test_crawl_SHOULD_return_crawled_url_list_WHEN_input_is_valid_url(mocked_urlopen):
    mocked_response = MagicMock()
    mocked_response.read.return_value = 'NORMAL RETURN'.encode()
    mocked_urlopen.return_value = mocked_response
    crawler = Crawler()
    crawler.set(1)

    actual = crawler.crawl(['VALID URL'])

    assert actual is not None
    assert type(actual) is list
    assert len(actual) == 1
