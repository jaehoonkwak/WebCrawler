import os
import shutil
from unittest.mock import MagicMock, patch

from pytest import fixture

import main.downloader

folder = "Downloads"


@fixture(autouse=True)
def run_around_tests():
    # Before
    remove_all_in_folder()

    yield

    # After
    remove_all_in_folder()


def remove_all_in_folder():
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


@patch('urllib.request.urlopen')
def test_download_SHOULD_do_download_WHEN_url_opened_normally(mocked_urlopen):
    mocked_response = MagicMock()
    mocked_response.getcode.return_value = 200
    mocked_response.read.return_value = 'TEST_CONTENTS'.encode()
    mocked_urlopen.return_value = mocked_response

    main.downloader.Downloader.download(["www.google.com"])

    with open('Downloads/0.html', 'r') as file:
        actual = file.readline()
        assert actual == 'TEST_CONTENTS'
