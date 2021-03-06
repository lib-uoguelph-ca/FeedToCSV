import threading
import queue
from requests.exceptions import ConnectionError as ce

"""
A downloader designed to work with the Internet Archive API.
This thread implements the pattern for stopping outlined here: 
    http://eli.thegreenplace.net/2011/12/27/python-threads-communication-and-stopping
"""


class IADownloaderThread(threading.Thread):
    retries = 3

    def __init__(self, id, queue, output_dir=None, logger=None):
        threading.Thread.__init__(self)
        self.queue = queue
        self.output_dir = output_dir
        self.id = id
        self.logger = logger
        # Essentially a synchronized flag that's set when the thread is asked to stop (join)
        self.stoprequest = threading.Event()

    def run(self):
        while not self.stoprequest.is_set():
            try:
                file = self.queue.get(timeout=0.5)
            except queue.Empty:
                continue

            try:
                self._download_file(file)
            except Exception:
                self.queue.task_done()
                self.queue.put(file)
                self.logger.warn("Requeue: {}".format(file.name))
                continue

            # send a signal to the queue that the job is done
            self.queue.task_done()

    """
    Public method to signal that the thread has been asked to stop
    """
    def stop(self):
        self.stoprequest.set()

    def _download_file(self, file):
        file.download(destdir=self.output_dir, retries=self.retries, checksum=True)
        msg = "Thread {id}: Downloaded {file}".format(id=self.id, file=file.name)
        self.logger.debug(msg)
