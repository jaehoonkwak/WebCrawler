import os
import shutil
import urllib.error
import urllib.parse
import urllib.request


class Downloader:

    download_folder = 'Downloads'

    @staticmethod
    def download(urls):
        Downloader.clean_directory(Downloader.download_folder)

        index = 0
        for url in urls:
            try:
                response = urllib.request.urlopen(url)
                html = response.read()

                filename = Downloader.download_folder + "/" + str(index) + ".html"
                with open(filename, "wb") as file:
                    file.write(html)
                    print("[Download][SUCCESS✅] URL='" + url + "' to '" + filename + "'")
                    index = index + 1
            except Exception as e:
                print("[Download][FAIL❌] URL='" + url + "' because of '" + str(e) + "'")

    @staticmethod
    def clean_directory(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
