import os
from urllib.request import urlopen

from threading import Thread


class DownloadThread(Thread):
    """
    A threading example that can download a file.
    """

    def __init__(self, url, name):
        """Initialize the thread"""
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        """Run the thread"""
        handle = urlopen(self.url)
        fname = os.path.basename(self.url)
        with open(fname, 'wb') as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        msg = "{} has finished downloading {}!".format(self.name, self.url)
        print(msg)


def main(urls):
    """
    Run the program.
    :param urls: List of Uniform Resource Locators to download.
    :return: None
    """
    for item, url in enumerate(urls):
        name = "Thread {}".format(item + 1)
        thread = DownloadThread(url, name)
        thread.start()


if __name__ == '__main__':
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    main(urls)
