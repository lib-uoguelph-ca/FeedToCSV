from .consumer import Consumer
import internetarchive as ia

class IAConsumer(Consumer):

    def __init__(self, transformer, writer, collection):
        #super().__init__(transformer, writer)
        self.collection = collection
        self.session = ia.get_session(config_file='ia.ini')
        self.item_ids = self._search()

    def process(self):
        for id in self.item_ids:
            item = self._get_item_metadata(id)
            self._download_files(id)

    def _get_item_metadata(self, item_id):
        item = ia.get_item(item_id, archive_session=self.session)
        metadata = item.metadata

        files = self._get_item_file_names(item_id)

        metadata['files'] = files

        return metadata

    def _download_files(self, item_id, output_path="./output"):
        files = self._get_item_files(item_id)
        for file in files:
            self._download_file(file, output_path)

    def _download_file(self, file, output_path="./output"):
        file.download(destdir=output_path)

    def _get_item_files(self, item_id, glob_pattern="*.pdf"):
        files_generator = ia.get_files(item_id, archive_session=self.session, glob_pattern=glob_pattern)
        files = [file for file in files_generator]
        return files

    def _get_item_file_names(self, item_id, glob_pattern="*.pdf"):
        files_generator = ia.get_files(item_id, archive_session=self.session, glob_pattern=glob_pattern)
        files = [file.name for file in files_generator]
        return files

    def _search(self):
        query = "collection:{}".format(self.collection)
        result = ia.search_items(query, archive_session=self.session)

        items = []
        for item in result:
            items.append(item['identifier'])

        return items