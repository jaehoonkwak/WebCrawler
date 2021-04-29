from unittest.mock import patch
import requests
from main.crawler import Crawler


@patch('requests.get')
def test_crawl_SHOULD_return_empty_list_WHEN_input_is_invalid_url(mock_get):
    mock_get.side_effect = requests.exceptions.MissingSchema
    assert len(Crawler.crawl(['w.google.com'])) == 0


@patch('requests.get')
def test_crawl_SHOULD_return_empty_listWHEN_input_is_valid_url(mock_get):
    mock_get.return_value = 'TEST'
    assert Crawler.crawl(['http://www.google.com']) == ['TEST']
