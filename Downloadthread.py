import threading
import requests

class DownloadThread(threading.Thread):
    def __init__(self, url, filename):
        super().__init__()
        self.url = url
        self.filename = filename

    def run(self):
        response = requests.get(self.url)
        with open(self.filename, 'wb') as f:
            f.write(response.content)


