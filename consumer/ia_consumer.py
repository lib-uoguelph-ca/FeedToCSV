from .consumer import Consumer
import internetarchive as ia
from downloader.threaded_downloader import ThreadedDownloader
from downloader.ia_downloader_thread import IADownloaderThread

class IAConsumer(Consumer):

    def __init__(self, transformer, writer, logger, collection, num_threads=4, output_dir="output", glob_pattern="*.pdf|*.txt"):
        self.transformer = transformer
        self.writer = writer
        self.logger = logger
        self.collection = collection
        self.session = ia.get_session(config_file='ia.ini')
        self.item_ids = self._search()
        self.item_ids.sort()
        self.num_threads = num_threads
        self.output_dir = output_dir
        self.glob_pattern = glob_pattern
        self.downloader = self._start_downloader(IADownloaderThread)

    # Instantiate threaded downloader
    def _start_downloader(self, downloader_thread_class):
        return ThreadedDownloader(num_threads=self.num_threads, thread_class=downloader_thread_class, output_dir=self.output_dir, logger=self.logger)

    # Iterate through the items,
    # * Build the metadata
    # * Write metadata to an output file
    # * Dowload the files associated with each item.
    def process(self):
        for id in self.item_ids:
            item = self._get_item_metadata(id)
            transformed = self.transformer.transform(item)
            self.writer.write(transformed)
            self._download_files(id, self.glob_pattern)

        self._cleanup()

    def _cleanup(self):
        self.downloader.stop()
        self.session.close()

    # Get and build a dictionary of metadata values for an item.
    def _get_item_metadata(self, item_id):
        item = ia.get_item(item_id, archive_session=self.session)
        metadata = item.metadata

        files = self._get_item_file_names(item_id)

        metadata['files'] = files

        return metadata

    # Download the files associated with an item.
    def _download_files(self, item_id, glob_pattern="*.pdf|*.txt"):
        files = self._get_item_files(item_id, glob_pattern)
        for file in files:
            self._download_file(file)

    # Add the file to the queue of objects we need to download
    def _download_file(self, file):
        queue = self.downloader.get_queue()
        queue.put(file)

    # Get the list of files associated with an item
    def _get_item_files(self, item_id, glob_pattern="*.pdf|*.txt"):
        files_generator = ia.get_files(item_id, archive_session=self.session, glob_pattern=glob_pattern)
        files = [file for file in files_generator]
        return files

    # Get a list of file names associated with an item
    def _get_item_file_names(self, item_id, glob_pattern="*.pdf|*.txt"):
        files_generator = ia.get_files(item_id, archive_session=self.session, glob_pattern=glob_pattern)
        files = [file.name for file in files_generator]
        return files

    # Search for items in a collection and return a list of item identifiers
    def _search(self):
        query = "collection:{}".format(self.collection)
        result = ia.search_items(query, archive_session=self.session)

        items = []
        for item in result:
            items.append(item['identifier'])

        return items