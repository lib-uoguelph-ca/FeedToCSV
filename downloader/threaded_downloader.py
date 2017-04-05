import os
import threading
import urllib.request
import queue

"""
 A generic downloader thread which draws from a queue of URLs to download.
"""


class URLDownloaderThread(threading.Thread):

    def __init__(self, id, queue, output_dir=None):
        """Initialize the thread"""
        threading.Thread.__init__(self)
        self.queue = queue
        self.output_dir = output_dir
        self.stoprequest = threading.Event()
        self.id = id

    def run(self):
        while not self.stoprequest.is_set():
            try:
                url = self.queue.get(timeout=0.5)
            except queue.Empty:
                continue

            self._download_file(url)

            # send a signal to the queue that the job is done
            self.queue.task_done()

    def stop(self):
        self.stoprequest.set()

    def _download_file(self, url):
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)

        # If needed, add the path to the target directory
        if self.output_dir is not None:
            fname = self.output_dir + os.sep + fname

        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f.write(chunk)
        msg = "Finished downloading %s!" % url
        print(msg)

"""
A class to manage threaded downloading of files, drawn from a queue.
Instantiate the class, then call get_queue() to get the queue, which can be used to add items to be downloaded.
When queue.empty() returns True, you're done downloading the files.
"""


class ThreadedDownloader:
    def __init__(self, num_threads=3, output_dir=None, thread_class=URLDownloaderThread):
        self.queue = queue.Queue()
        self.num_threads = num_threads
        self.output_dir = output_dir
        self.threads = []
        self.thread_class = thread_class
        self._init_threads()

    def get_queue(self):
        return self.queue

    def _init_threads(self):
        for i in range(self.num_threads):
            thread = self.thread_class(i, self.queue, self.output_dir)
            self.threads.append(thread)
            thread.start()

    def stop(self):
        self.queue.join() # Blocks until all unfinished items have been processed.
        self._cleanup()

    def _cleanup(self):
        for thread in self.threads:
            thread.stop()
