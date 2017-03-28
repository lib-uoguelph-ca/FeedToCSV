import threading

"""
A downloader designed to work with the Internet Archive API.
This thread impelents the pattern for stopping outlined here: 
    http://eli.thegreenplace.net/2011/12/27/python-threads-communication-and-stopping
"""


class IADownloaderThread(threading.Thread):

    def __init__(self, queue, output_dir=None):
        threading.Thread.__init__(self)
        self.queue = queue
        self.output_dir = output_dir
        # Essentially a synchronized flag that's set when the thread is asked to stop (join)
        self.stoprequest = threading.Event()

    def run(self):
        while not self.stoprequest.isSet():
            file = self.queue.get()
            self._download_file(file)

            # send a signal to the queue that the job is done
            self.queue.task_done()

    def join(self, timeout=None):
        self.stoprequest.set()
        super(IADownloaderThread, self).join(timeout)

    def _download_file(self, file):
        file.download(destdir=self.output_dir)
        msg = "Downloaded %s!" % file.name
        print(msg)
